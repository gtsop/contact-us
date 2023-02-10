from typing import Literal
from enum import Enum
from pydantic import BaseSettings

class Settings(BaseSettings):
    storage_db_uri: str = "sqlite:///:memory:"
    storage_strategy: Literal["in-memory"] | Literal["database"] = "in-memory"
    transmitter_strategy: Literal["std-out"] | Literal["no-op"] | Literal["email"] = "std-out"
