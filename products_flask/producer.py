import datetime

import pika
import os
import json

URL = os.environ.get('URL')

params = pika.URLParameters(URL)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()


def publish(method, body):
    """Producer publish method"""
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',
                          routing_key='admin',
                          body=json.dumps(body),
                          properties=properties,
                          )
