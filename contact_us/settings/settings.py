from typing import Literal
from enum import Enum
from pydantic import BaseSettings

class Settings(BaseSettings):
    storage_db_uri: str = "sqlite:///:memory:"
    storage_strategy: Literal["in_memory"] | Literal["db_storage"] = "in_memory"
