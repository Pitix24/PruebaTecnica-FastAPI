import pika
import json

class AuthCommandConsumer:
    def __init__(self, rabbitmq_url, login_use_case, logout_use_case):
        self.connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='auth_commands')
        self.login_use_case = login_use_case
        self.logout_use_case = logout_use_case

    def start_consuming(self):
        def callback(ch, method, properties, body):
            data = json.loads(body)
            if data.get("type") == "login":
                self.login_use_case.execute(data)
            elif data.get("type") == "logout":
                self.logout_use_case.execute(data)
        self.channel.basic_consume(queue='auth_commands', on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()
