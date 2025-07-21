import pika 
import json

class UserCommandProducer:
    def __init__(self, rabbitmq_url):
        self.connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='user_commands')

    def send_create_user_command(self, command_data):
        self.channel.basic_publish(
            exchange='',
            routing_key='user_commands',
            body=json.dumps(command_data)
        )
