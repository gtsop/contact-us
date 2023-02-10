from contact_us.app.message import Message
from contact_us.testing import are_messages_equal
from .in_memory_storage import InMemoryStorage

from ..storage_test import abstract_test_storage


def test_in_memory_storage():
    def create_storage():
        return InMemoryStorage()
    abstract_test_storage(create_storage)


def test_in_momory_storage_looses_data_across_instances():
    message = Message("a", "b")

    storageA = InMemoryStorage()
    storageA.append(message)
    assert are_messages_equal(storageA.all(), [message])

    storageB = InMemoryStorage()
    assert are_messages_equal(storageB.all(), [])
