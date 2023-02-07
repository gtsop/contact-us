from .in_memory_storage import InMemoryStorage

from .storage_test import abstract_test_storage

def test_in_memory_storage():
    abstract_test_storage(InMemoryStorage)