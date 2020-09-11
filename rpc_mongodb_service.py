#!/usr/bin/env python
import math
import argparse
from collections import deque

from pymongo import MongoClient

import pika

parser = argparse.ArgumentParser(description='Rabbitmq RPC corpus channel')
parser.add_argument('--collection')
args = parser.parse_args()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

DB_HOST = '172.17.0.1'
DB_PORT = 27017
DB_USER = 'bottrainer'
DB_UPASS = '111'

qsize = 400
d = deque(maxlen=qsize)


def opt_collection(client):
    collection = args.collection
    if not collection:
        raise Exception("No mongodb database specified")

    if collection == 'thefinal':
        db = client.thefinal
        return db.docs

    raise Exception("Invalid mongodb database name")


def count_documents(dbcollection):
    return dbcollection.count_documents({})


def corpus_buf():
    with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
        dbcollection = opt_collection(client)

        total = count_documents(dbcollection)
        batch_size = 4000
        start_index = 0
        for index in range(0, math.ceil(total / batch_size)):
            start_index = index * batch_size
            end_index = start_index + batch_size if (start_index + batch_size) < total else total
            cursor = dbcollection.find(projection={"_id": False})
            reviews_batch = list(cursor[start_index:end_index])

            if not len(reviews_batch):
                raise StopIteration

            for line in reviews_batch:
                yield str(line['tag']) + "]|[" + line['text']


def channel_buf():

    while True:
        result = d.pop()
        d.appendleft(next(corpus_buffer))

        yield result


def on_request(ch, method, props, body):
    response = next(channel_buffer)

    ch.basic_publish(exchange='', routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


corpus_buffer = corpus_buf()

channel_buffer = channel_buf()

for i in range(qsize):
    d.appendleft(next(corpus_buffer))


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()

