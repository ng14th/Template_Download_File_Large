import pika

def clear_message_in_XQ():
    parameters = pika.URLParameters('amqp://admin:admin@172.27.230.14:5672/nguyennt63')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    result = channel.queue_purge(queue='file_handler.XQ')

    print(f"Number of messages purged: {result.method.message_count}")