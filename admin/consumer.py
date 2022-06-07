import datetime

import pika, os, json, django
django.setup()


from products.models import Product


URL = os.environ.get('URL')
params = pika.URLParameters(URL)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)

    product.likes = product.likes + 1
    print(f'Product likes increased : {product.likes} ')
    product.save()
    print(f'Product likes increased : {product.likes} ')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=False)

print('Started Consuming')

channel.start_consuming()

channel.close()
