from enum import Enum

from contact_us.app.message import Message
from contact_us.app.transmitter import Transmitter
from contact_us.app.storage import Storage, InMemoryStorage, DatabaseStorage


class App:
    def __init__(self, transmitter: Transmitter, storage: Storage):
        self.transmitter = transmitter
        self.storage = storage

    def create_message(self, email, body):
        message = Message(email=email, body=body)
        self.storage.append(message)
        return message

    def send_message(self, message):
        self.transmitter.transmit(message)
        message.send()
        self.storage.update(message)

    def list_messages(self):
        return self.storage.all()

    def list_unsent_messages(self):
        return [m for m in self.storage.all() if not m.is_sent]


def create_app(transmitter: type[Transmitter], storage: type[Storage]) -> App:
    return App(transmitter=transmitter(), storage=storage())
