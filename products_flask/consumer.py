import pika
import os

URL = os.environ.get('URL')

params = pika.URLParameters(URL)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('recived in main linux')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
