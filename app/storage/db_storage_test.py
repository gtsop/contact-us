from .db_storage import DBStorage
from app.message import Message
from app.__test_utils__ import are_messages_equal

def test_db_storage_instantiates():
    assert DBStorage()

def test_db_storage_method_append():
    message = Message('a', 'b')
    
    storage = DBStorage()
    storage.append(message)

def test_db_storage_method_all():

    messageA = Message('foo', 'bar')
    messageB = Message('bar', 'baz')

    storage1 = DBStorage()
    storage1.append(messageA)

    storage2 = DBStorage()
    storage2.append(messageB)

    storage3 = DBStorage()
    assert are_messages_equal(storage3.all(), [messageA, messageB])
