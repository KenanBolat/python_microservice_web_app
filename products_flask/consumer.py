import pika

URL = "amqps://hjfiwhei:GligQtV6UAojYH_J9Hno_JAec43PcfLA@goose.rmq2.cloudamqp.com/hjfiwhei"
params = pika.URLParameters(URL)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('recived in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)


print('Started Consuming')

channel.start_consuming()


channel.close()