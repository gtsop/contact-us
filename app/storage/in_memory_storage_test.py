from .in_memory_storage import InMemoryStroage
from app.message import Message

def test_in_memory_storage_instantiates():
    assert InMemoryStroage()

def test_in_memory_storage_method_append():
    storage = InMemoryStroage()
    message = Message()
    storage.append(message)

def test_in_memory_storage_method_all():
    storage = InMemoryStroage()

    messageA = Message()
    messageB = Message()

    storage.append(messageA)
    storage.append(messageB)

    assert storage.all() == [messageA, messageB]