import pika
import json

class UserCommandConsumer:
    def __init__(self, rabbitmq_url, create_user_use_case):
        self.connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='user_commands')
        self.create_user_use_case = create_user_use_case

    def start_consuming(self):
        def callback(ch, method, properties, body):
            data = json.loads(body)
            self.create_user_use_case.execute(data)
        self.channel.basic_consume(queue='user_commands', on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()
