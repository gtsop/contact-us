from typing import List
from contact_us.app.message import Message
from .storage import Storage

class InMemoryStorage(Storage):
    def __init__(self):
        self.messages: List[Message] = []

    def append(self, message: Message):
        self.messages.append(message)
    
    def all(self):
        return self.messages
    
    def update(self, message: Message):
        pass
