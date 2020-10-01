import csv
import os
import re
import argparse

import logging
import pprint

from datetime import datetime
from datetime import date

import numpy as np
from gensim.models import Doc2Vec

from doc2vec_service import query_semantic_distance


def verify_infering_vector(model_fpath=None, model=None, epochs=50, example=None):
    if not example:
        example = "while driving down the street he sees a girl on a bicycle"

    tokens = example.split(' ')

    if model:
        _model = model
    elif model_fpath:
        _model = Doc2Vec.load(model_fpath)
    else:
        raise Exception("No model file path or model instance provided!")

    vector = _model.infer_vector(tokens, epochs=epochs)

    ntimes = 10000
    min = 100
    max = 0
    total_diff = 0
    length = 0
    for i in range(ntimes):
        __vec__ = _model.infer_vector(tokens, epochs=epochs)
        difference_vector = __vec__ - vector
        difference = np.linalg.norm(difference_vector)
        min = difference if difference < min else min
        max = difference if difference > max else max
        total_diff += difference
        length += np.linalg.norm(vector)

    length = length / ntimes
    averg_difference = total_diff / ntimes
    relative = 100 * averg_difference / length

    print('Epochs=%d' % epochs)
    print('Difference - min: %f; max: %f; avg: %f' % (min, max, averg_difference))
    print('Average length: %f' % (length))
    print('Difference over vector length: %03.1f' % (relative))


def assess_rational_inference(model, model_fpath, forder, epochs, threshold, baseline=65, is_silent=False):
    has_result = False
    is_pass = False
    score = 0
    count = 0

    info = "\n"
    info += "\n--------------------------------------------------------------------"
    info += '\n<FILE %d>: %s' % (forder, str(model_fpath))
    info += '\n\t<PARAMETERS>: EPOCHS=%d - THRESHOLD=%05.3f' % (epochs, threshold)
    info += "\n--------------------------------------------------------------------"

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
                is_good = '(*)' if distance > threshold else ' ~ '
                score += 1 if distance > threshold else 0
            else:
                is_good = '(*)' if distance < threshold else ' ~ '
                score += 1 if distance < threshold else 0

            info += "\n%s | %s :: %s | (wrt theme: %s), distance=%f" % (is_good, query, target, theme, distance)

        score_percent = 100 * score / count
        is_pass = score_percent > 89

        info += '\n<< SCORE: %05.2f >>' % (score_percent)
        info += '\n* *** *  << PASSED >> * *** *' if is_pass else ''

        # default value 65
        if score_percent > baseline:
            has_result = True

            if not is_silent:
                logger.info(info)
                print(info)

    return (has_result, score_percent)


def setup_hyperparameters():
    EPOCHS = [10, 20, 50, 75, 100, 150, 200]
    THRESHOLD = np.arange(0.25, 0.95, 0.025)

    hyperparameters = []
    for ep in EPOCHS:
        for thres in THRESHOLD:
            hyperparameters.append((ep, thres))

    return hyperparameters


def assess_rational_inference_over_hyperparameters(model_fpath, forder):

    model = Doc2Vec.load(model_fpath)
    hyperparameters = setup_hyperparameters()

    has_result = False
    max_score = 0

    for epochs, threshold in hyperparameters:
        result, score = assess_rational_inference(
                                    model=model,
                                    model_fpath=model_fpath,
                                    forder=forder,
                                    epochs=epochs,
                                    threshold=threshold
                            )
        has_result = has_result | result

        max_score = score if score > max_score else max_score

    return has_result, max_score


def assess_stable_performance(model_fpath, forder=999, ntimes=10, baseline=50):
    model = Doc2Vec.load(model_fpath)
    hyperparameters = setup_hyperparameters()

    is_stable = True
    logger.info(model_fpath)
    for epochs, threshold in hyperparameters:

        logger.info('\n')
        logger.info('Parameters: epochs=%d, threshold=%05.3f' % (epochs, threshold))

        for i in range(ntimes):
            result, _ = assess_rational_inference(
                            model=model,
                            model_fpath=model_fpath,
                            forder=forder,
                            epochs=epochs,
                            threshold=threshold,
                            baseline=60,
                            is_silent=True
                        )
            is_stable = is_stable & result
            logger.info('<LOOP - %d> %s' % (i, str(result)))

        if is_stable:
            print('\n')
            print('Parameters: epochs=%d, threshold=%05.3f' % (epochs, threshold))
            print('* *** *  << STABLE >> * *** *')

            logger.info('* *** *  << STABLE >> * *** *')

        else:
            logger.info('Failed!')


def assess_all_model():

    forder = 1
    dirpath = 'models/'
    qualified = []
    for f in os.listdir(dirpath):
        if re.match(r".+\.bin$", f):
            model_fpath = dirpath + f
            has_result, max_score = assess_rational_inference_over_hyperparameters(
                            model_fpath=model_fpath,
                            forder=forder
                            )
            forder += 1

            if not has_result:
                print("\n```````````````````````````````````````````````````````````````````````````")
                print("(!) %d - Model has bad result: %s" % (forder, model_fpath))
                print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n")

                logger.info("\n```````````````````````````````````````````````````````````````````````````")
                logger.info("(!) %d Model has bad result: %s" % (forder, model_fpath))
                logger.info(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n")
            else:
                qualified.append("%s - max score: %04.2f" % (f, max_score))

    print("\n")
    print("-----------------------------------------------------------------------")
    print("<SUMMARIZATION>:")
    pprint.pprint(qualified,  width=160)

    logger.info("\n")
    logger.info("<SUMMARIZATION>:")
    logger.info('\n'.join(qualified))


def register_logging_handler(logger, name):
    now = datetime.now()
    today = date.today()
    resultfile = "logs/{}h{}m{}_{}.txt".format(str(today), now.hour, now.minute, name)
    hdlr = logging.FileHandler(resultfile)
    logger.addHandler(hdlr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rabbitmq RPC corpus channel')
    parser.add_argument('--cmd', type=int, default=0)
    args = parser.parse_args()

    # NOTES: epochs = 100, the value results in good result

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if args.cmd == 0:
        register_logging_handler(logger, 'assess_all_model')
        assess_all_model()

    if args.cmd == 1:
        register_logging_handler(logger, 'assess_stable_performance')
        assess_stable_performance(
                    model_fpath='models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin',
                    ntimes=3
                )
    if args.cmd == 3:
        verify_infering_vector(
                    model_fpath='models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin',
                    epochs=50,
                    example='a huge car'
                )
