#!/usr/bin/env python
import math
import argparse
import time
import pickle
from collections import deque, namedtuple

from pymongo import MongoClient
import bson

import _thread
import pika

SentimentDocument = namedtuple('SentimentDocument', 'words tags')

parser = argparse.ArgumentParser(description='Rabbitmq RPC corpus channel')
parser.add_argument('--database')
args = parser.parse_args()

# credentials = pika.PlainCredentials('myrabbit', '111')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', heartbeat=0))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

DB_HOST = '172.17.0.1'
DB_PORT = 27017
DB_USER = 'bottrainer'
DB_UPASS = '111'

BATCH_SIZE = 100000
BUFFER_NUMBER = 100
END_SIGNAL = '<!END!>'


def opt_collection(client):
    database = args.database
    if not database:
        raise Exception("No mongodb database specified")

    if database == 'thefinal':
        db = client.thefinal
        return db.docs

    if database == 'enwik9':
        db = client.enwik9
        return db.docs

    raise Exception("Invalid mongodb database name")


def count_documents(dbcollection):
    return dbcollection.count_documents({})


def data_buf():
    with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
        dbcollection = opt_collection(client)
        total = count_documents(dbcollection)

        while True:
            count = 1
            for index in range(0, math.ceil(total / BATCH_SIZE)):
                print("Caching batch index: %d" % (index))

                batches = dbcollection.find_raw_batches({'batch_index': index}, projection={"_id": False, "batch_index": False})

                for batch in batches:
                    yield batch

                count += 1

            print("\n")
            print('<END>: %d batches of document have been served.' % (count))
            print("------------------------------------")

            yield END_SIGNAL


def stack_data(__buffer, d):
    while True:
        if len(d) < math.floor(BUFFER_NUMBER / 1.1):
            while len(d) < BUFFER_NUMBER:
                result = next(__buffer)
                d.appendleft(result)
                print('Stacked item, cache buffer length %d' % (len(d)))

        time.sleep(0.1)


def get_data(d):
    while True:
        if len(d):
            result = d.pop()
            print('Pop, cache buffer length %d' % (len(d)))

            return result

        time.sleep(0.1)


def on_request(ch, method, props, body, d):
    response = get_data(d)

    ch.basic_publish(exchange='', routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_request_wrapper(d):
    def callback(ch, method, props, body):
        on_request(ch, method, props, body, d)
    return callback


def main():
    d = deque(maxlen=BUFFER_NUMBER)
    buffer = data_buf()
    _thread.start_new_thread(stack_data, (buffer, d))

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='rpc_queue', on_message_callback=on_request_wrapper(d))

    print(" [x] Awaiting RPC requests")
    channel.start_consuming()


if __name__ == "__main__":
    main()

