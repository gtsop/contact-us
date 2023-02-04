from .in_memory_storage import InMemoryStorage
from app.message import Message

def test_in_memory_storage_instantiates():
    assert InMemoryStorage()

def test_in_memory_storage_method_append():
    storage = InMemoryStorage()
    message = Message()
    storage.append(message)

def test_in_memory_storage_method_all():
    storage = InMemoryStorage()

    messageA = Message()
    messageB = Message()

    storage.append(messageA)
    storage.append(messageB)
