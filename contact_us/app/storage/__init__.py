from .storage import Storage
from .strategies.in_memory_storage import InMemoryStorage
from .strategies.database_storage import DatabaseStorage
from contact_us.settings import settings

class StorageStrategies:
    InMemory: type[Storage] = InMemoryStorage
    Database: type[Storage] = DatabaseStorage

    @staticmethod
    def setting() -> type[Storage]:
        if settings.storage_strategy == 'in-memory':
            return InMemoryStorage
        if settings.storage_strategy == 'database':
            return DatabaseStorage
        return InMemoryStorage



