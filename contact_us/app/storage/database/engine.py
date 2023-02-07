from sqlalchemy import create_engine
from contact_us.settings import settings

SQLALCHEMY_DATABASE_URL = settings.storage_db_uri

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)