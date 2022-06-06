import datetime

import pika
import os
import json

URL = os.environ.get('URL')
params = pika.URLParameters(URL)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Recieved in Admin linux')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
