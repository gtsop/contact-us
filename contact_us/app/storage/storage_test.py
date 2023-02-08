from typing import Callable
from contact_us.app.message import Message
from contact_us.testing import are_messages_equal
from .storage import Storage

def abstract_test_storage_instantiates(storage: Storage):
    assert storage

def abstract_test_storage_method_append(storage: Storage):
    message = Message('a', 'b')
    storage.append(message)

def abstract_test_storage_method_all(storage: Storage):
    messageA = Message('a', 'b')
    messageB = Message('b', 'c')

    storage.append(messageA)
    storage.append(messageB)

    assert are_messages_equal(storage.all(), [messageA, messageB])

def abstract_test_storage(create_storage: Callable[[], Storage]):
    abstract_test_storage_instantiates(create_storage())
    abstract_test_storage_method_append(create_storage())
    abstract_test_storage_method_all(create_storage())