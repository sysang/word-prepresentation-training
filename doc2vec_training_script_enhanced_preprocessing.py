# coding: utf-8
import io
import re
import tarfile
import os
import multiprocessing
import math
import collections

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

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


SentimentDocument = collections.namedtuple('SentimentDocument', 'words tags')

DB_HOST = '172.17.0.1'
DB_PORT = 27017
DB_USER = 'bottrainer'
DB_UPASS = '111'


class MyCorpus(object):
    def __init__(self, name):
        self.dataset = name
        self.total_count = self.count()

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

    def __iter__(self):
        with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
            dbcollection = self._opt_collection(client)

            total = self.total_count
            batch_size = 50000
            start_index = 0
            for index in range(0, math.ceil(total / batch_size)):
                start_index = index * batch_size
                end_index = start_index + batch_size if (start_index + batch_size) < total else total
                cursor = dbcollection.find(projection={"_id": False})
                reviews_batch = list(cursor[start_index:end_index])

                for line in reviews_batch:
                    yield SentimentDocument(line['text'].split(' '), [int(line['tag'])])

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


def train(name, common_kwargs, saved_fname, evaluate=False):
    alldocs = MyCorpus(name)

    simple_models = [
        # PV-DM w/ concatenation - big, slow, experimental mode
        # window=5 (both sides) approximates paper's apparent 10-word total window size
        Doc2Vec(workers=5, **common_kwargs),
    ]

    if not evaluate:
        for model in simple_models:
            model.build_vocab(alldocs)
            print("%s vocabulary scanned & state initialized" % model)
            model.train(alldocs, total_examples=alldocs.total_count, epochs=model.epochs)
    else:
        simple_models = [
            # PV-DM w/ concatenation - big, slow, experimental mode
            # window=5 (both sides) approximates paper's apparent 10-word total window size
            Doc2Vec.load(saved_fname),
        ]

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
        random_index, random_doc = alldocs.get_random_doc()
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
    print(u'TARGET (%d): %s\n' % (doc_id, alldocs.get_doc_by_index(doc_id)))
    print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % (str(model)))
    for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
        s = sims[index]
        i = int(sims[index][0])
        words = alldocs.get_doc_by_index(i)
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
