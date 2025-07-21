import pika
import json

class AuthCommandProducer:
    def __init__(self, rabbitmq_url):
        self.connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='auth_commands')

    def send_login_command(self, command_data):
        self.channel.basic_publish(
            exchange='',
            routing_key='auth_commands',
            body=json.dumps(command_data)
        )

    def send_logout_command(self, command_data):
        self.channel.basic_publish(
            exchange='',
            routing_key='auth_commands',
            body=json.dumps(command_data)
        )
