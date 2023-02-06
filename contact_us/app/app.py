from typing import Type
from contact_us.app.message import Message
from contact_us.app.transmitter import Transmitter
from contact_us.app.storage import Storage, InMemoryStorage


class App:
    def __init__(
        self, transmitter: Type[Transmitter], storage: type[Storage] = InMemoryStorage
    ):
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
