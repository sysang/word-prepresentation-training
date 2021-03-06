import csv
import os
import re
import argparse
import time
import math

import logging
import pprint

from datetime import datetime
from datetime import date

import numpy as np
from gensim.models import Doc2Vec

from doc2vec_service import query_semantic_distance
from doc2vec_service import model_infer_vector


def verify_infering_vector(model_fpath=None, model=None, epochs=5, nsamples=300, example=None):
    if not example:
        example = "while driving down the street he sees a girl on a bicycle"

    tokens = example.split(' ')

    if model:
        _model = model
    elif model_fpath:
        _model = Doc2Vec.load(model_fpath)
    else:
        raise Exception("No model file path or model instance provided!")

    vector = model_infer_vector(model=_model, tokens=tokens, epochs=epochs, nsamples=nsamples)

    ntimes = 1000
    min = 1e6
    max = 0
    total_diff = 0
    now = time.time()
    differences = []
    total_length = 0
    for i in range(ntimes):
        __vec__ = model_infer_vector(model=_model, tokens=tokens, epochs=epochs, nsamples=nsamples)
        difference_vector = __vec__ - vector
        difference = np.linalg.norm(difference_vector)
        differences.append(difference)
        min = difference if difference < min else min
        max = difference if difference > max else max
        total_diff += difference
        total_length += np.linalg.norm(__vec__)

    averg_difference = total_diff / ntimes
    relative = 100 * total_diff / total_length
    averg_range = 100 * ntimes * (max - min) / total_length

    standard_deviation = 0
    for diff in differences:
        standard_deviation += math.pow((diff - averg_difference), 2)
    deviation = math.sqrt(standard_deviation / ntimes)
    averg_deviation = 100 * deviation * ntimes / total_length

    print('Epochs=%d; nsamples=%d' % (epochs, nsamples))
    print('Execution time: %05.3f(s)' % ((time.time() - now) / ntimes))
    print('(Difference) diff/length: %f / %f = %05.2f(%%)' % (diff, total_length, relative))
    print('(Difference) range: %05.2f(%%)' % (averg_range))
    print('(Difference) deviation: %05.3f(%%)' % (averg_deviation))


def assess_rational_inference(model, model_fpath, forder, epochs, threshold, baseline=65, is_silent=False):
    ambigity_compensation = 0.1
    has_result = False
    is_pass = False
    score = 0
    count = 0
    confidence = 0

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
            direction = float(row[3]) > 0  # determine how we infer meaning from comparison with threshold
            distance = query_semantic_distance(
                    model=model,
                    query=query,
                    target=target,
                    theme=theme,
                    epochs=epochs,
                )

            is_true = False
            not_sure = False
            if distance > threshold * (1 + ambigity_compensation):
                is_true = direction
                score += 1 if is_true else 0
            elif distance < threshold * (1 - ambigity_compensation):
                is_true = not direction
                score += 1 if is_true else 0
            else:
                not_sure = True
                confidence -= 1

            indicator = ('(*)' if is_true else ' ~ ') if not not_sure else ' ? '
            info += "\n%s | %s :: %s | (wrt theme: %s), distance=%f" % (indicator, query, target, theme, distance)

        score_percent = 100 * score / count
        confidence_percent = 100 * (confidence + count) / count
        is_pass = score_percent > 89

        info += '\n<< SCORE: %05.2f >>' % (score_percent)
        info += '\n<< CONFIDENCE: %05.2f >>' % (confidence_percent)
        info += '\n* *** *  << PASSED >> * *** *' if is_pass else ''

        # default value 65
        if score_percent > baseline:
            has_result = True

            if not is_silent:
                logger.info(info)
                print(info)

    return (has_result, score_percent)


def setup_hyperparameters():
    EPOCHS = [3, 4, 5, 6]
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


def assess_stable_performance(model_fpath, forder=999, ntimes=10, baseline=50, is_silent=True):
    model = Doc2Vec.load(model_fpath)
    hyperparameters = setup_hyperparameters()

    logger.info(model_fpath)
    for epochs, threshold in hyperparameters:

        logger.info('\n')
        logger.info('Parameters: epochs=%d, threshold=%05.3f' % (epochs, threshold))

        unstable_level = math.ceil(ntimes - ntimes * 0.8)
        failed_count = 0
        for i in range(ntimes):
            result, _ = assess_rational_inference(
                            model=model,
                            model_fpath=model_fpath,
                            forder=forder,
                            epochs=epochs,
                            threshold=threshold,
                            baseline=60,
                            is_silent=is_silent
                        )

            if not result:
                failed_count += 1
            is_stable = failed_count <= unstable_level

            logger.info('<LOOP - %d> %s' % (i, str(result)))

            if not is_stable:
                break

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
                    model_fpath='models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_blogwikgutimdb.bin',
                    ntimes=20,
                    is_silent=False
                )
    if args.cmd == 2:
        verify_infering_vector(
                    model_fpath='models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_blogwikgutimdb.bin',
                    epochs=3,
                    nsamples=300,
                    # example='a huge car'
                )
