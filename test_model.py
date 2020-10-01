import csv
import os
import re

import numpy as np
from gensim.models import Doc2Vec

from doc2vec_service import query_semantic_distance


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


def assess_the_rational_inference(model_fpath, forder, hyperparameters):

    model = Doc2Vec.load(model_fpath)
    has_result = False

    for epochs, threshold in hyperparameters:

        result = "\n"
        result += "\n--------------------------------------------------------------------"
        result += '\n<FILE %d>: %s' % (forder, str(model_fpath))
        result += '\n<PARAMETERS>: EPOCHS=%d - THRESHOLD=%05.2f' % (epochs, threshold)
        result += "\n--------------------------------------------------------------------"

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
            result += '\n<< SCORE>: %05.2f >>' % (score_percent)
            result += '\n* *** *  << PASSED >> * *** *' if is_pass else ''
            if score_percent > 65:
                has_result = True
                print(result)

    return has_result


def assess_all_model():

    EPOCHS = [10, 20, 50, 100, 200]
    THRESHOLD = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    hyperparameters = []
    for ep in EPOCHS:
        for thres in THRESHOLD:
            hyperparameters.append((ep, thres))

    forder = 1
    dirpath = 'models/'
    for f in os.listdir(dirpath):
        if re.match(r".+\.bin$", f):
            model_fpath = dirpath + f
            has_result = assess_the_rational_inference(
                            model_fpath=model_fpath,
                            forder=forder,
                            hyperparameters=hyperparameters)
            forder += 1

            if not has_result:
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                print("## Model has no result: %s ##\n" % (model_fpath))
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")


if __name__ == "__main__":
    # NOTES: epochs = 100, the value results in good result

    assess_all_model()
