import time
import csv
import os
import re

import numpy as np
from gensim.models import Doc2Vec

EPOCHS = 300


def verify_infering_vector(_model, epochs=5, example=None):
    if not example:
        example = "while driving down the street he sees a girl on a bicycle"

    tokens = example.split(' ')

    n = 1000
    min = 100
    max = 0
    sum = 0
    length = 0
    for i in range(n):
        # time.sleep(0.1)
        vector = _model.infer_vector(tokens, epochs=epochs)
        __vec__ = _model.infer_vector(tokens, epochs=epochs)
        d = np.dot(vector, __vec__)/(np.linalg.norm(vector) * np.linalg.norm(__vec__))
        min = d if d < min else min
        max = d if d > max else max
        length += np.linalg.norm(vector)
        sum += abs(d)

    length = length / n
    print('min: %f; max: %f; avg: %f' % (min, max, sum / n))
    print('Average vector length: %f' % (length))


def magniture_on(query, target):
    return np.sum(query * target)/np.linalg.norm(target)


def semantic_comparision(model, query, target, theme):
    query_vector = model.infer_vector(query.split(' '), epochs=EPOCHS)
    target_vector = model.infer_vector(target.split(' '), epochs=EPOCHS)
    theme_vector = model.infer_vector([theme], epochs=EPOCHS)
    query_mag_on_theme = magniture_on(query_vector, theme_vector)
    target_mag_on_theme = magniture_on(target_vector, theme_vector)
    sim = abs(target_mag_on_theme - query_mag_on_theme) / np.linalg.norm(theme_vector)

    return sim


def assess_the_rational_inference(model_fpath):
    print("\n")
    print("--------------------------------------------------------------------")
    print('<FILE>: %s' % str(model_fpath))
    print("--------------------------------------------------------------------")

    model = Doc2Vec.load(model_fpath)

    with open('sentence_semantics_queries.csv', newline='') as f:
        rows = csv.reader(f, delimiter=';', quotechar='|')
        for row in rows:
            query = row[0]
            target = row[1]
            theme = row[2]
            threshold = float(row[3])
            sim = semantic_comparision(
                    model=model,
                    query=query,
                    target=target,
                    theme=theme
                )
            if threshold > 0:
                is_good = '[*]' if sim > threshold else ' ~ '
            else:
                is_good = '[*]' if sim < abs(threshold) else ' ~ '

            print("%s %s - %s, distance score: %f, with respect to theme: %s" % (is_good, query, target, sim, theme))


def assess_all_model():
    dirpath = 'models/'
    for f in os.listdir(dirpath):
        if re.match(r".+\.bin$", f):
            model_fpath = dirpath + f
            assess_the_rational_inference(model_fpath)


if __name__ == "__main__":

    # verify_infering_vector(model, EPOCHS)
    assess_all_model()
