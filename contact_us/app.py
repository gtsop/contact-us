from contact_us.message import Message
from contact_us.transmitter import Transmitter
from contact_us.storage import Storage, InMemoryStorage

class App:

    def __init__(self, transmitter: Transmitter, storage: Storage = InMemoryStorage):
        self.transmitter = transmitter()
        self.storage = storage()

    def create_message(self, email, body):
        message = Message(email=email, body=body)
        self.storage.append(message)
        return message

    def send_message(self, message):
        self.transmitter.transmit(message)
        message.send()

    def list_messages(self):
        return self.storage.all()
    
    def list_unsent_messages(self):
        return [m for m in self.storage.all() if not m.is_sent]