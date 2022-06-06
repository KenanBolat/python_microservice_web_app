import datetime

import pika

import os

import json

from products.models import Product

URL = os.environ.get('URL')
params = pika.URLParameters(URL)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=id)

    product.likes = product.likes + 1
    print(f'Product likes increased : {product.likes} ')
    product.save()
    print(f'Product likes increased : {product.likes} ')


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
