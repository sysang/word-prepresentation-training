from collections import defaultdict
from gensim import corpora
from gensim import models
import gensim
import smart_open

import pprint
pp = pprint.PrettyPrinter(indent=4)

# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import os


class MyCorpus(object):
    def __iter__(self):
        for line in open('corpus/mycorpus.txt'):
            yield line.lower().split()


def learn_processing_corpus():

    text_corpus = MyCorpus()

    # Create a set of frequent words
    stoplist = set('for a an of the and to in'.split(' '))

    # Lowercase each document, split it by white space and filter out stopwords
    texts = [[word for word in document if word not in stoplist] for document in text_corpus]

    # Count word frequencies
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    # Only keep words that appear more than once
    processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
    dictionary = corpora.Dictionary(processed_corpus)
    pp.pprint(list(dictionary.values()))

    pp.pprint(dictionary.token2id)
    # dictionary.save('tmp/deerwester.dict')

    bow_corpus = [dictionary.doc2bow(text) for text in texts]
    # corpora.MmCorpus.serialize('tmp/deerwester.mm', bow_corpus)  # store to disk, for later use
    pp.pprint(bow_corpus)

    new_doc = "Human computer interaction"
    new_vec = dictionary.doc2bow(new_doc.lower().split())
    pp.pprint(new_vec)


def load_dictionary_and_print_corpus():
    # doesn't load the corpus into memory!
    corpus_memory_friendly = MyCorpus()
    # # load one vector into memory at a time
    dictionary = corpora.Dictionary.load('tmp/deerwester.dict')
    for document in corpus_memory_friendly:
        print(dictionary.doc2bow(document))


def transform_corpus():
    dictionary = corpora.Dictionary.load('tmp/deerwester.dict')
    # learn_processing_corpus()
    # load_dictionary_and_print_corpus()
    bow_corpus = corpora.MmCorpus('tmp/deerwester.mm')
    tfidf = models.TfidfModel(bow_corpus)

    corpus_tfidf = tfidf[bow_corpus]
    lsi_model = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)  # initialize an LSI transformation
    corpus_lsi = lsi_model[corpus_tfidf]  # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
    # lsi_model.print_topics(2)

    # for doc in corpus_tfidf:
    # pp.pprint(doc)


def read_corpus(fname, tokens_only=False):
    with smart_open.open(fname, encoding='iso-8859-1') as f:
        for i, line in enumerate(f):
            tokens = gensim.utils.simple_preprocess(line)
            if tokens_only:
                yield tokens
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(tokens, [i])


def doc2vec():
    # Set file names for train and test data
    test_data_dir = os.path.join(gensim.__path__[0], 'test', 'test_data')
    lee_train_file = os.path.join(test_data_dir, 'lee_background.cor')
    lee_test_file = os.path.join(test_data_dir, 'lee.cor')

    train_corpus = list(read_corpus(lee_train_file))
    test_corpus = list(read_corpus(lee_test_file, tokens_only=True))

    model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40)
    model.build_vocab(train_corpus)
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)

    vector = model.infer_vector(['only', 'you', 'can', 'prevent', 'forest', 'fires'])
    pp.pprint(vector)


doc2vec()
