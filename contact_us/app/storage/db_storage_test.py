from contact_us.app.message import Message
from contact_us.testing import are_messages_equal, create_temp_create_session
from .db_storage import DBStorage

from .storage_test import abstract_test_storage


def test_db_storage():
    abstract_test_storage(DBStorage)


def test_db_storage_persists_data_across_instances():
    create_session = create_temp_create_session()

    message = Message("a", "b")

    storageA = DBStorage(create_session)
    storageA.append(message)
    assert are_messages_equal(storageA.all(), [message])

    storageB = DBStorage(create_session)
    assert are_messages_equal(storageB.all(), [message])
