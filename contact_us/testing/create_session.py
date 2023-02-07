from typing import Callable, Tuple
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker
import tempfile

def create_session(sqlurl: str = "sqlite:///:memory:") -> Tuple[Session, Engine]:
    engine = create_engine(sqlurl, connect_args={"check_same_thread": False})
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session(), engine


def create_temp_create_session() -> Callable[[], Tuple[Session, Engine]]:
    temp_dir = tempfile.mkdtemp()

    def temp_create_session() -> Tuple[Session, Engine]:
        sqlurl = f"sqlite:///{temp_dir}/app.db"
        return create_session(sqlurl)

    return temp_create_session
