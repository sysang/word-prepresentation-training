# coding: utf-8
import math
import collections
import argparse
import time
import csv

from gensim.models.doc2vec import Doc2Vec
import numpy as np

from pymongo import MongoClient

from multiprocessing import Process, Value, Queue
import ctypes

import pika
import uuid
import pickle

from doc2vec_service import query_semantic_distance
from test_model import verify_infering_vector

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

DB_HOST = '127.0.0.1'
DB_PORT = 27017
DB_USER = 'bottrainer'
DB_UPASS = '111'

RABBITMQ_HOST = 'localhost'

BUFFER_NUMBER = 5

BATCH_SIZE = 100000
END_SIGNAL = '<!END!>'

SentimentDocument = collections.namedtuple('SentimentDocument', 'words tags')

# credentials = pika.PlainCredentials('myrabbit', '111')

parser = argparse.ArgumentParser(description='Rabbitmq RPC corpus channel')
parser.add_argument('--database', required=True)
parser.add_argument('--check-dataset', type=int, dest='check_dataset', default=False)
args = parser.parse_args()


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
    def __init__(self, queue_buffers, buffer_size_status, buffer_emptiness_status):
        self.total_count = self.count()
        self.queue_buffers = queue_buffers
        self.buffer_size_status = buffer_size_status
        self.buffer_emptiness_status = buffer_emptiness_status
        self.iteration_index = 0

    def __iter__(self):
        rotator = len(self.queue_buffers)

        while True:
            next_order = self.iteration_index % rotator
            # buffer = self.queue_buffers[next_order]
            is_full = self.buffer_size_status[next_order]
            is_empty = self.buffer_emptiness_status[next_order]

            if not is_full.value:
                # print('<WAITING...> %s' % (next_order))
                time.sleep(0.01)
                continue

            # print('\t\t\t<UNLOADING...> %s' % (next_order))
            docs = pickle.loads(self.queue_buffers[next_order].get())

            if docs[0]['text'] == END_SIGNAL:
                print('----------------------------------')
                print('<CORPUS ITERATOR> End of dataset.')
                print("----------------------------------")
                is_full.value = False
                is_empty.value = True
                self.iteration_index += 1
                break

            for doc in docs:
                yield SentimentDocument(doc['text'].split(' '), [int(doc['tag'])])

            is_full.value = False
            is_empty.value = True
            # print('\t\t\t<LOADED> %s' % (next_order))
            # print('\t\t\t<STATUS> %s' % ([b.value for b in self.buffer_size_status]))
            self.iteration_index += 1

    def get_doc_by_index(self, index):
        with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
            dbcollection = opt_collection(client)
            review = dbcollection.find_one({'tag': index})

            return review['text']

    def count(self):
        with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
            dbcollection = opt_collection(client)

            return dbcollection.count_documents({})

    def get_random_doc(self):
        random_index = np.random.randint(self.total_count)
        print(".....get random document, tag: " + str(random_index))

        return random_index, self.get_doc_by_index(random_index)


def opt_collection(client):
    database = args.database
    if not database:
        raise Exception("No mongodb database specified")

    if database == 'refined':
        db = client.refined
        return db.docs

    # refined
    if database == 'blogwikgutimdb':
        db = client.blogwikgutimdb
        return db.docs

    if database == 'thefinal':
        db = client.thefinal
        return db.docs

    if database == 'enwik9':
        db = client.enwik9
        return db.docs

    if database == 'enwik8':
        db = client.enwik8
        return db.docs

    if database == 'bloggercom':
        db = client.bloggercom
        return db.posts

    raise Exception("Invalid mongodb database name")


def pick_random_word(model, threshold=1000):
    # pick a random word with a suitable number of occurences
    while True:
        word = np.random.choice(model.wv.index2word)
        if model.wv.vocab[word].count > threshold:
            return word


def count_documents(dbcollection):
    return dbcollection.count_documents({})


def mongo_buf():
    with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
        dbcollection = opt_collection(client)
        total = count_documents(dbcollection)

        while True:
            count = 0
            for index in range(0, math.ceil(total / BATCH_SIZE)):
                # print("<MONGO CLIENT> Caching batch index: %d" % (index))

                batch = dbcollection.find(
                        {'batch_index': index},
                        projection={"_id": False, "batch_index": False},
                        no_cursor_timeout=True
                    )

                count += 1
                yield list(batch)

            print("---------------------------------------------------")
            print('<END>: %d mini batches of document have been served.' % (count))
            print("---------------------------------------------------")

            yield [{'text': END_SIGNAL, 'tag': -1}]


def rpc_buf(rpc_client):
    while True:
        response = rpc_client.call()
        if not response:
            raise StopIteration("Can not get data from rpc server.")

        yield response


def thread_data_buffer(queue_buffers, buffer_size_status, buffer_emptiness_status):
    data_buffer = mongo_buf()
    rotator = len(queue_buffers)

    index = 0
    while True:
        next_order = index % rotator
        # buffer = queue_buffers[next_order]
        is_full = buffer_size_status[next_order]
        is_empty = buffer_emptiness_status[next_order]

        if not is_empty.value:
            # print("<SLEEPING> %s" % (next_order))
            time.sleep(0.01)
            continue

        # print('<STACKING ...> %s' % (next_order))
        response = next(data_buffer)
        queue_buffers[next_order].put(pickle.dumps(response))

        is_full.value = True
        is_empty.value = False
        index += 1
        # print('<SENT> %s' % (next_order))
        # print('<STATUS> %s' % ([b.value for b in buffer_size_status]))


def sanity_check_datasource(mycorpus):
    try:
        while True:
            next = 0
            tag = 0
            for doc in mycorpus:
                tag = doc.tags[0]
                if tag != next:
                    print("tag - %s vs next - %s" % (tag, next))
                    raise Exception("There is a break in data source.")
                next = tag + 1

            print("** DONE *** Last tag: %s" % (tag))
            print("\n")
    except Exception as error:
        print(doc)
        raise error


def train(common_kwargs, saved_fname, database, evaluate=False):
    database = args.database
    if database != args.database:
        raise "Database settings are mismatched!"

    queue_buffers = []
    buffer_size_status = []
    buffer_emptiness_status = []
    for i in range(BUFFER_NUMBER):
        queue_buffers.append(Queue(maxsize=1))
        buffer_size_status.append(Value(ctypes.c_bool, False))
        buffer_emptiness_status.append(Value(ctypes.c_bool, True))

    multi_process = Process(target=thread_data_buffer, args=(queue_buffers, buffer_size_status, buffer_emptiness_status))
    multi_process.daemon = True
    multi_process.start()
    print("Start child process for buffering data, PID %s" % (multi_process.pid))

    mycorpus = MyCorpus(queue_buffers, buffer_size_status, buffer_emptiness_status)

    if args.check_dataset:
        sanity_check_datasource(mycorpus)

    model = Doc2Vec(workers=6, queue_factor=4, **common_kwargs)

    if not evaluate:
        model.build_vocab(mycorpus)
        print("%s vocabulary scanned & state initialized" % model)

        model.train(mycorpus, total_examples=mycorpus.total_count, epochs=model.epochs)

        print("\n")
        print('----------------------------------')
        print('<FINISHED TRAINING>')
        print("----------------------------------")
    else:
        model = Doc2Vec.load(saved_fname)

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
    print('\tEXAMINING THE MODEL')
    print("\n")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    # Store model
    # -------------------------------------------------------------
    print("\n")
    print("INFO: Training parameters: " + str(common_kwargs))
    print("INFO: Model details: " + str(model))
    print("INFO: Save model to: " + saved_fname)

    model.save(saved_fname)

    # Terminate data buffering process
    multi_process.terminate()

    # Are inferred vectors close to the precalculated ones?
    # -------------------------------------------------------
    print("\n")
    print("-----------------------------------------------------")
    print("Are inferred vectors close to the precalculated ones?")
    print("-----------------------------------------------------")

    topn = 200
    for ind in range(0, 7):
        random_index, random_doc = mycorpus.get_random_doc()
        print('-> index %s --> "%s"' % (random_index, random_doc))

        inferred_docvec = model.infer_vector(random_doc.split(' '))
        similarities = model.docvecs.most_similar([inferred_docvec], topn=topn)
        rank = 1
        for (index, score) in similarities:
            if index == random_index:
                print('[*] Matched with rank %s, score: %s!' % (rank, score))
                print("\n")
                break
            rank += 1
        if rank == topn + 1:
            print("    No any match in top %s similarities." % (topn))
            print("\n")

    # Do close documents seem more related than distant ones?
    # -------------------------------------------------------
    print("\n")
    print("-----------------------------------------------------")
    print("Do close documents seem more related than distant ones?")
    print("-----------------------------------------------------")

    doc_id = np.random.randint(model.docvecs.count)  # pick random doc, re-run cell for more examples
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

    for ind in range(0, 7):
        target_word = pick_random_word(model)
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
    print("\n")

    # grab the file if not already local
    questions_filenames = ['questions-words-narrowed.txt']
    for questions_filename in questions_filenames:
        # Note: this analysis takes many minutes
        print("[+] " + questions_filename)
        score, sections = model.wv.evaluate_word_analogies(questions_filename)
        correct, incorrect = len(sections[-1]['correct']), len(sections[-1]['incorrect'])
        print('%s: %0.2f%% correct (%d of %d)' % (model, float(correct*100)/(correct+incorrect), correct, correct+incorrect))
        print("\n")

    # Benchmark against analogies metric baseline
    # -------------------------------------------------------------
    print("\n")
    print("-----------------------------------------------------")
    print("Benchmark against analogies metric baseline")
    print("-----------------------------------------------------")

    # 01 - wordsim353
    print("\n")
    print("01 - wordsim353")

    result = model.wv.evaluate_word_pairs('wordsim353.tsv')
    print(result)

    # 02 - simlex999
    print("\n")
    print("02 - simlex999")

    result = model.wv.evaluate_word_pairs('simlex999.txt')
    print(result)

    # 03 - simverb3500
    print("\n")
    print("03 - simverb3500")

    result = model.wv.evaluate_word_pairs('simverb3500_DGerz.txt')
    print(result)

    print("\n")
    print("-----------------------------------------------------")
    print("Assess stability of inferencing vector")
    print("-----------------------------------------------------")
    print("\n")

    verify_infering_vector(model=model, epochs=5, nsamples=300)

    print("\n")
    print("-----------------------------------------------------")
    print("Benchmark similarity score with respect to theme word")
    print("-----------------------------------------------------")
    print("\n")

    EPOCHS = [3]
    THRESHOLD = np.arange(0.25, 0.35, 0.05)
    ambigity_compensation = 0.1
    confidence = 0
    for epochs in EPOCHS:
        for threshold in THRESHOLD:

            with open('sentence_semantics_queries.csv', newline='') as f:
                rows = csv.reader(f, delimiter=';', quotechar='|')

                score = 0
                count = 0
                for row in rows:
                    count += 1
                    query = row[0]
                    target = row[1]
                    theme = row[2]
                    direction = float(row[3]) > 0  # determine how we infer meaning from comparison with threshold
                    distance = query_semantic_distance(
                            model=model,
                            query=query,
                            target=target,
                            theme=theme,
                            epochs=epochs,
                        )
                    is_true = False
                    if distance > threshold * (1 + ambigity_compensation):
                        is_true = direction
                        score += 1 if is_true else 0
                    elif distance < threshold * (1 - ambigity_compensation):
                        is_true = not direction
                        score += 1 if is_true else 0
                    else:
                        confidence -= 1

                score_percent = 100 * score / count
                confidence_percent = 100 * (confidence + count) / count
                if score > 10:
                    print('<EPOCHS: %d - THRESHOLD: %05.2f> - SCORE=%05.2f - CONFIDENCE=%05.2f' % (epochs, threshold,  score_percent, confidence_percent))
                    print('\n')

    print("\n")
    print("_____  COMPLETED  _________________________________")
    print("###~~~~~~~~#~~~~~~~#~~~~~~~#~~~~~~~~~~#~~~~~~~~~###")
    print("\n")
