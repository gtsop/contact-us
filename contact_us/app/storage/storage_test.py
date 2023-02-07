from contact_us.app.message import Message
from contact_us.testing import are_messages_equal
from .storage import Storage

def abstract_test_storage_instantiates(storage_class: type[Storage]):
    assert storage_class()

def abstract_test_storage_method_append(storage_class: type[Storage]):
    message = Message('a', 'b')
    
    storage = storage_class()
    storage.append(message)

def abstract_test_storage_method_all(storage_class: type[Storage]):
    storage = storage_class()

    messageA = Message('a', 'b')
    messageB = Message('b', 'c')

    storage.append(messageA)
    storage.append(messageB)

    assert are_messages_equal(storage.all(), [messageA, messageB])

def abstract_test_storage(storage_class: type[Storage]):
    abstract_test_storage_instantiates(storage_class)
    abstract_test_storage_method_append(storage_class)
    abstract_test_storage_method_all(storage_class)