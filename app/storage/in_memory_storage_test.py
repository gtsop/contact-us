from .in_memory_storage import InMemoryStorage
from app.message import Message
from app.__test_utils__ import are_messages_equal

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

    assert are_messages_equal(storage.all(), [messageA, messageB])
