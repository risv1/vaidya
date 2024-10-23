import pika 

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def recieve_message():
    connection = pika.BlockingConnection
    (pika.ConnectionParameters(
        'localhost', 5672, '/', 
        pika.PlainCredentials('rabbitmq', 'rabbitmq')))
    
    channel = connection.channel()

    channel.queue_declare(queue='inc')

    channel.basic_consume(queue='inc',
                        auto_ack=True,
                        on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()