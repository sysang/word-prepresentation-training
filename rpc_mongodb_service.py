#!/usr/bin/env python
import math
import argparse
import time
from collections import deque

from pymongo import MongoClient

import _thread
import pika

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

qsize = 25000
batch_size = 100000
buffer_number = 50
d = deque(maxlen=buffer_number)


def opt_collection(client):
    database = args.database
    if not database:
        raise Exception("No mongodb database specified")

    if database == 'thefinal':
        db = client.thefinal
        return db.docs

    raise Exception("Invalid mongodb database name")


def count_documents(dbcollection):
    return dbcollection.count_documents({})


def data_buf():
    while True:
        with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
            dbcollection = client.thefinal.docs

            total = count_documents(dbcollection)

            count = 1
            for index in range(0, math.ceil(total / batch_size)):
                print("Caching batch index: %d" % (index))

                cursor = dbcollection.find({'batch_index': index}, projection={"_id": False})
                reviews_batch = list(cursor)
                loaded = len(reviews_batch)
                if not loaded:
                    raise StopIteration("Stop data buffering iteration because of empty response.")

                volume = 0
                result = ''
                for line in reviews_batch:
                    doc = str(line['tag']) + ']~[' + line['text']
                    result += '>|<' + doc
                    volume += 1
                    count += 1
                    if volume >= qsize or (count + volume) > total:
                        yield result[3:]
                        volume = 0
                        result = ''

            yield '<!END!>'
            print('DEBUG: last batch volume %d' % (loaded))
            print('DEBUG: last  volume %d' % (volume))
            print('DEBUG: %d documents have been served.' % (count))


def stack(__buffer):
    while True:
        if len(d) < math.floor(buffer_number / 1.1):
            while len(d) < buffer_number:
                result = next(__buffer)
                d.appendleft(result)
                print('Stacked item of length %d, current length %d' % (len(result), len(d)))
                pass
        pass


def get_data():
    while True:
        if len(d):
            result = d.pop()
            print('Pop, current length %d' % (len(d)))

            return result
        pass


def on_request(ch, method, props, body, buffer):
    response = get_data()

    ch.basic_publish(exchange='', routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

    print('Start stacking data...')


def on_request_wrapper(buffer):
    def callback(ch, method, props, body):
        on_request(ch, method, props, body, buffer)
    return callback


buffer = data_buf()
_thread.start_new_thread(stack, (buffer,))
# for i in range(buffer_number):
#     stack(buffer)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request_wrapper(buffer))

print(" [x] Awaiting RPC requests")
channel.start_consuming()

