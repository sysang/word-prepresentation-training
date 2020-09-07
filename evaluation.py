from gensim import models
from gensim.test.utils import datapath

import pprint
pp = pprint.PrettyPrinter(indent=4)

def run(model_file, target='go', comparison='went'):
    model = models.Doc2Vec.load(model_file)

    result = model.wv.evaluate_word_pairs(datapath('wordsim353.tsv'))
    pp.pprint(result)

    if target:
        result = model.wv.most_similar(target.split(' '))
        pp.pprint(result)
    if target and comparison:
        result = model.wv.n_similarity(target.split(' '), comparison.split(' '))
        pp.pprint(result)
        result = model.wv.wmdistance(target.split(' '), comparison.split(' '))
        pp.pprint(result)

    return model

