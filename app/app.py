from app.message import Message
from app.transmitter import Transmitter

class App:

    def __init__(self, transmitter: Transmitter):
        self.messages = list()
        self.transmitter = transmitter

    def create_message(self, email, body):
        message = Message(email=email, body=body)
        self.messages.append(message)
        return message

    def send_message(self, message):
        self.transmitter.transmit(message)
        message.send()

    def list_messages(self):
        return self.messages
    
    def list_unsent_messages(self):
        return [m for m in self.messages if not m.is_sent]