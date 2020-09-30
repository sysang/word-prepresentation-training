import time
import csv
import os
import re

import numpy as np
from gensim.models import Doc2Vec

from doc2vec_service import query_semantic_distance

# NOTES: epochs = 100, the value results in good result
EPOCHS = 100


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


def assess_the_rational_inference(model_fpath, order):
    print("\n")
    print("--------------------------------------------------------------------")
    print('<FILE %d>: %s' % (order, str(model_fpath)))
    print("--------------------------------------------------------------------")

    model = Doc2Vec.load(model_fpath)

    for epochs in [10, 20, 50, 100, 200]:

        result = '\nEPOCHS=%d' % (epochs)
        is_pass = True
        score = 0
        count = 0

        with open('sentence_semantics_queries.csv', newline='') as f:

            rows = csv.reader(f, delimiter=';', quotechar='|')

            for row in rows:
                count += 1
                query = row[0]
                target = row[1]
                theme = row[2]
                direction = float(row[3])
                distance = query_semantic_distance(
                        model=model,
                        query=query,
                        target=target,
                        theme=theme,
                        epochs=epochs,
                    )

                # threshold = abs(direction)
                threshold = 0.4
                if direction > 0:
                    is_good = '[*]' if distance > threshold else ' ~ '
                    is_pass = is_pass & (distance > threshold)
                    score += 1 if distance > threshold else 0
                else:
                    is_good = '[*]' if distance < threshold else ' ~ '
                    is_pass = is_pass & (distance < threshold)
                    score += 1 if distance < threshold else 0

                result += "\n%s %s - %s, distance score: %f, with respect to theme: %s" % (is_good, query, target, distance, theme)

            score_percent = 100 * score / count
            result += '\n<SCORE>: %05.2f' % (score_percent)
            result += '\n* *** *  << PASSED >> * *** *' if is_pass else ''
            if score_percent > 60:
                print(result)


def assess_all_model():
    order = 1
    dirpath = 'models/'
    for f in os.listdir(dirpath):
        if re.match(r".+\.bin$", f):
            model_fpath = dirpath + f
            assess_the_rational_inference(model_fpath, order)
            order += 1


if __name__ == "__main__":
    # verify_infering_vector(model, EPOCHS)

    assess_all_model()
