import pika

def send_message(message):
    connection = pika.BlockingConnection
    (pika.ConnectionParameters(
        'localhost', 5672, '/', 
        pika.PlainCredentials('rabbitmq', 'rabbitmq')))
    
    channel = connection.channel()

    channel.queue_declare(queue='inc')

    channel.basic_publish(exchange='',
                        routing_key='inc',
                        body=message)
    
    print(f" [x] Sent {message}")

    connection.close()