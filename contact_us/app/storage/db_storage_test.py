from .db_storage import DBStorage

from contact_us.testing import create_temp_create_session
from contact_us.app.message import Message
from contact_us.__test_utils__ import are_messages_equal

def test_db_storage_instantiates():
    assert DBStorage()

def test_db_storage_method_append():
    message = Message('a', 'b')
    
    storage = DBStorage()
    storage.append(message)

def test_db_storage_method_all():

    create_session = create_temp_create_session()

    messageA = Message('foo', 'bar')
    messageB = Message('bar', 'baz')

    storage1 = DBStorage(create_session)
    storage1.append(messageA)

    storage2 = DBStorage(create_session)
    storage2.append(messageB)

    storage3 = DBStorage(create_session)
    assert are_messages_equal(storage3.all(), [messageA, messageB])
