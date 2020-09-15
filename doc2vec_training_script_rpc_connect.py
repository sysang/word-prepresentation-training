# coding: utf-8
import io
import re
import tarfile
import os
import multiprocessing
import math
import collections
import time
from multiprocessing import Process, Manager

from gensim.utils import simple_preprocess
from gensim.utils import to_unicode
from gensim.models.doc2vec import Doc2Vec
import gensim.utils
import gensim.models.doc2vec
import numpy as np

from collections import OrderedDict
import smart_open
from pymongo import MongoClient
import pymongo

import pika
import uuid

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

DB_HOST = '172.17.0.1'
DB_PORT = 27017
DB_USER = 'bottrainer'
DB_UPASS = '111'

RABBITMQ_HOST = 'localhost'

# set the item in 1 buffer, too big value will slow down the loop
# this will multiple buffering cache to (n)times of RPC server package size
BUFFER_SIZE = 10

BUFFER_NUMBER = 3

SentimentDocument = collections.namedtuple('SentimentDocument', 'words tags')

# credentials = pika.PlainCredentials('myrabbit', '111')


class CorpusRpcClient(object):

    def __init__(self, host, credentials=None):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, heartbeat=0))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body='')

        while self.response is None:
            self.connection.process_data_events()

        return self.response


class MyCorpus(object):
    def __init__(self, name, multithread_buffers):
        self.dataset = name
        self.total_count = self.count()
        self.multithread_buffers = multithread_buffers
        self.buffer_number = len(multithread_buffers)

    def _opt_collection(self, client):
        if self.dataset == 'imdb':
            db = client.imdb_reviews
            return db.reviews

        if self.dataset == 'blog':
            db = client.bloggercom
            return db.posts

        if self.dataset == 'wiki':
            db = client.enwik8
            return db.docs

        if self.dataset == 'mycorus':
            db = client.mycorus
            return db.docs

        if self.dataset == 'thefinal':
            db = client.thefinal
            return db.docs

        raise Exception("No valid database")

    def create_document_tag(self, response):
        response = response.decode('utf-8')
        if response == ('<!END!>'):
            raise StopIteration

        splited = response.split('>|<')
        for doc in splited:
            tag, text = doc.split(']~[', 1)
            yield SentimentDocument(text.split(' '), [int(tag)])

    def __iter__(self):
        try:
            index = 0
            while True:
                nextind = index % self.buffer_number

                if len(self.multithread_buffers[nextind]) < BUFFER_SIZE:
                    time.sleep(0.1)
                    continue

                time.sleep(0.01)
                buffer = self.multithread_buffers[nextind]
                while len(buffer) > 0:
                    response = buffer.pop()
                    tag_documents = self.create_document_tag(response)
                    for doc in tag_documents:
                        yield doc

                index += 1

        except Exception:
            pass

    def get_doc_by_index(self, index):
        with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
            dbcollection = self._opt_collection(client)
            review = dbcollection.find_one({'tag': index})

            return review['text']

    def count(self):
        with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
            dbcollection = self._opt_collection(client)

            return dbcollection.count_documents({})

    def get_random_doc(self):
        random_index = np.random.randint(self.total_count)
        print(".....get random document, tag: " + str(random_index))

        return random_index, self.get_doc_by_index(random_index)


def pick_random_word(model, threshold=1000):
    # pick a random word with a suitable number of occurences
    while True:
        word = np.random.choice(model.wv.index2word)
        if model.wv.vocab[word].count > threshold:
            return word


def get_data(rpc_client):
    while True:
        response = rpc_client.call()
        if not response:
            raise StopIteration("Can not get data from rpc server.")

        yield response


def thread_data_buffer(rpc_client, multithread_buffers):
    iterable_data = get_data(rpc_client)
    buffer_number = len(multithread_buffers)
    index = 0

    while True:
        # print('~~~~~~~~~~~~~~~~~~~~~ I AM DOING NOTHING! ~~~~~~~~~~~~~~~~~~~~~~')
        nextind = index % buffer_number

        if len(multithread_buffers[nextind]) > 0:
            time.sleep(0.1)
            continue

        buffer = multithread_buffers[nextind]
        while len(buffer) < BUFFER_SIZE:
            buffer.append(next(iterable_data))

        index += 1


def train(name, common_kwargs, saved_fname, evaluate=False):

    rpc_client = CorpusRpcClient(RABBITMQ_HOST)

    multithread_buffers = []
    for i in range(BUFFER_NUMBER):
        multithread_buffers.append(Manager().list())

    multi_process = Process(target=thread_data_buffer, args=(rpc_client, multithread_buffers))
    multi_process.start()

    mycorpus = MyCorpus(name, multithread_buffers)

    simple_models = [
        # PV-DM w/ concatenation - big, slow, experimental mode
        # window=5 (both sides) approximates paper's apparent 10-word total window size
        Doc2Vec(workers=8, queue_factor=4, **common_kwargs),
    ]

    if not evaluate:
        for model in simple_models:
            model.build_vocab(mycorpus)
            print("%s vocabulary scanned & state initialized" % model)
            model.train(mycorpus, total_examples=mycorpus.total_count, epochs=model.epochs)
    else:
        simple_models = [
            # PV-DM w/ concatenation - big, slow, experimental mode
            # window=5 (both sides) approximates paper's apparent 10-word total window size
            Doc2Vec.load(saved_fname),
        ]

    multi_process.join()

    # EXAMINING RESULTS
    #
    # Let's look for answers to the following questions:
    # . Are inferred vectors close to the precalculated ones?
    # . Do close documents seem more related than distant ones?
    # . Do the word vectors show useful similarities?
    # . Are the word vectors from this dataset any good at analogies?
    # . Are inferred vectors close to the precalculated ones?
    # -----------------------------------------------------
    print("\n")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\n")
    print('EXAMINING RESULTS')
    print("\n")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    # Store model
    # -------------------------------------------------------------
    count = len(simple_models)
    ind = 0
    for model in simple_models:
        ind += 1
        save_to = saved_fname + (str(ind) if count > 1 else '')
        print("\n")
        print("Model details: " + str(model))
        print("Save model to: " + save_to)

        model.save(save_to)

    # Are inferred vectors close to the precalculated ones?
    # -------------------------------------------------------
    print("\n")
    print("-----------------------------------------------------")
    print("Are inferred vectors close to the precalculated ones?")
    print("-----------------------------------------------------")

    topn = 100
    for ind in range(0, 7):
        random_index, random_doc = mycorpus.get_random_doc()
        print('[+] index %s -> "%s"' % (random_index, random_doc))
        for model in simple_models:
            inferred_docvec = model.infer_vector(random_doc.split(' '))
            similarities = model.docvecs.most_similar([inferred_docvec], topn=topn)
            rank = 1
            for (index, score) in similarities:
                if index == random_index:
                    print('** Matched with rank %s, score: %s' % (rank, score))
                    print("\n")
                    break
                rank += 1
            if rank == topn + 1:
                print("!! No any match in top %s similarities" % (topn))
                print("\n")

    # Do close documents seem more related than distant ones?
    # -------------------------------------------------------
    print("\n")
    print("-----------------------------------------------------")
    print("Do close documents seem more related than distant ones?")
    print("-----------------------------------------------------")

    doc_id = np.random.randint(simple_models[0].docvecs.count)  # pick random doc, re-run cell for more examples
    model = simple_models[0]
    sims = model.docvecs.most_similar(doc_id, topn=model.docvecs.count)  # get *all* similar documents
    print(u'TARGET (%d): %s\n' % (doc_id, mycorpus.get_doc_by_index(doc_id)))
    print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % (str(model)))
    for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
        s = sims[index]
        i = int(sims[index][0])
        words = mycorpus.get_doc_by_index(i)
        print(u'%s %s: «%s»\n' % (label, s, words))

    # Do the word vectors show useful similarities?
    # ---------------------------------------------
    print("\n")
    print("-----------------------------------------------------")
    print("Do the word vectors show useful similarities?")
    print("-----------------------------------------------------")

    for ind in range(0, 5):
        target_word = pick_random_word(simple_models[0])
        for model in simple_models:
            print('[+] target_word: %r model: %s:' % (target_word, model))
            for i, (word, sim) in enumerate(model.wv.most_similar(target_word, topn=7), 1):
                print('     %d. %.2f %r' % (i, sim, word))
            print("\n")

    # Are the word vectors from this dataset any good at analogies?
    # -------------------------------------------------------------

    print("\n")
    print("-----------------------------------------------------")
    print("Are the word vectors from this dataset any good at analogies?")
    print("-----------------------------------------------------")

    # grab the file if not already local
    questions_filename = 'questions-words.txt'
    if not os.path.isfile(questions_filename):
        # Download IMDB archive
        print("Downloading analogy questions file...")
        url = u'https://raw.githubusercontent.com/tmikolov/word2vec/master/questions-words.txt'
        with smart_open.open(url, 'rb') as fin:
            with smart_open.open(questions_filename, 'wb') as fout:
                fout.write(fin.read())
    assert os.path.isfile(questions_filename), "questions-words.txt unavailable"

    # Note: this analysis takes many minutes
    for model in simple_models:
        score, sections = model.wv.evaluate_word_analogies('questions-words.txt')
        correct, incorrect = len(sections[-1]['correct']), len(sections[-1]['incorrect'])
        print('%s: %0.2f%% correct (%d of %d)' % (model, float(correct*100)/(correct+incorrect), correct, correct+incorrect))

    # Benchmark against analogies metric baseline
    # -------------------------------------------------------------
    print("\n")
    print("-----------------------------------------------------")
    print("Benchmark against analogies metric baseline")
    print("-----------------------------------------------------")

    # 01 - wordsim353
    print("\n")
    print("01 - wordsim353")

    for model in simple_models:
        result = model.wv.evaluate_word_pairs('wordsim353.tsv')
        print(result)

    # 02 - simlex999
    print("\n")
    print("02 - simlex999")

    for model in simple_models:
        result = model.wv.evaluate_word_pairs('simlex999.txt')
        print(result)

    # 03 - simverb3500
    print("\n")
    print("03 - simverb3500")

    for model in simple_models:
        result = model.wv.evaluate_word_pairs('simverb3500_DGerz.txt')
        print(result)

    print("\n")
    print("             ____________     COMPLETED          ___________________________      ")
    print("#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#")
    print("\n")
