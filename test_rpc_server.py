#!/usr/bin/env python
import pika
import uuid

credentials = pika.PlainCredentials('myrabbit', '111')
host = "172.19.0.2"


class MongodbRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, credentials=credentials))

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


fibonacci_rpc = MongodbRpcClient()

response = fibonacci_rpc.call()

if not response:
    print("Client should stop iteration")
else:
    print(" [.] Got %s" % response)
