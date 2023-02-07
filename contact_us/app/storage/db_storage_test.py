from .db_storage import DBStorage

from .storage_test import abstract_test_storage

def test_db_storage():
    abstract_test_storage(DBStorage)