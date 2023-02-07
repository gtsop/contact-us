from pydantic import BaseSettings

class Settings(BaseSettings):
    storage_db_uri: str = 'sqlite:///:memory:'