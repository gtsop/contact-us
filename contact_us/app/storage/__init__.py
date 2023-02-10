from .storage import Storage
from .strategies.in_memory_storage import InMemoryStorage
from .strategies.database_storage import DatabaseStorage

STORAGE_STRATEGIES = {
    "InMemory": InMemoryStorage,
    "Database": DatabaseStorage
}