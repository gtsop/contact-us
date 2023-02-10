from contact_us.app.message import Message
from contact_us.testing import are_messages_equal, create_session, create_temp_create_session
from .database_storage import DatabaseStorage

from ..storage_test import abstract_test_storage


def test_db_storage():
    def create_storage():
     return DatabaseStorage(create_session)
    abstract_test_storage(create_storage)


def test_db_storage_persists_data_across_instances():
    create_session = create_temp_create_session()

    message = Message("a", "b")

    storageA = DatabaseStorage(create_session)
    storageA.append(message)
    assert are_messages_equal(storageA.all(), [message])

    storageB = DatabaseStorage(create_session)
    assert are_messages_equal(storageB.all(), [message])
