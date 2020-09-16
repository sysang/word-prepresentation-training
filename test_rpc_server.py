#!/usr/bin/env python
import pika
import uuid
import pickle
import bson
from bson.codec_options import CodecOptions

import collections

credentials = pika.PlainCredentials('myrabbit', '111')
host = "localhost"


class MongodbRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body='')
        while self.response is None:
            self.connection.process_data_events()
        return self.response


db_client = MongodbRpcClient()


def test_concatenating_method():
    while True:
        response = db_client.call()

        if not response:
            raise StopIteration("Response is empty")

        try:
            response = response.decode('utf-8')
            splited = response.split('>|<')

            next, _ = splited[0].split(']~[', 1)
            next = int(next)
            print("first tag of batch:  %d" % (next))

            for s in splited:
                tag, _ = s.split(']~[', 1)
                if int(tag) != next:
                    print("tag - %s vs next - %s" % (tag, next))
                    raise Exception("There is bug in data source.")
                next = int(tag) + 1

            print("last tag of batch:   %s" % (tag))

        except Exception as e:
            print("RESPONSE: " + response)
            # raise e


def test_pickle_method():
    try:
        while True:
            response = db_client.call()

            if not response:
                raise StopIteration("Response is empty")

            # print(response)
            data = pickle.loads(response)
            if data == '<!END!>':
                print(data)

    except Exception as error:
        print(data)
        raise error


def test_bson_method():
    try:
        while True:
            response = db_client.call()

            if not response:
                raise StopIteration("Response is empty")

            # print(response)

            if response == bytearray('<!END!>', "utf8"):
                print(response)
            else:
                data = bson.decode_all(response)
                print(data[0])
    except Exception as error:
        print(response)
        raise error


if __name__ == "__main__":
    # test_pickle_method()
    test_bson_method()
