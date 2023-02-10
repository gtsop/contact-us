from typing import Tuple, Callable
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker

from contact_us.settings import settings
from contact_us.app.message import Message

from ..models import BaseModel, MessageModel
from ..storage import Storage


def session_factory() -> Tuple[Session, Engine]:
    engine = create_engine(
        settings.storage_db_uri, connect_args={"check_same_thread": False}
    )
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session(), engine


class DatabaseStorage(Storage):
    def __init__(
        self, create_session: Callable[[], Tuple[Session, Engine]] = session_factory
    ):
        self.db, self.engine = create_session()
        BaseModel.metadata.create_all(bind=self.engine)

    def __del__(self):
        self.db.close()

    def append(self, message: Message):
        db_message = MessageModel.from_message(message)
        self.db.add(db_message)
        self.db.commit()
        self.db.refresh(db_message)
        return db_message

    def update(self, message: Message):
        db_message = (
            self.db.query(MessageModel)
            .filter(MessageModel.email == message.email)
            .filter(MessageModel.body == message.body)
            .first()
        )
        if db_message:
            db_message.is_sent = message.is_sent
            self.db.commit()

    def all(self):
        return [entry.to_message() for entry in self.db.query(MessageModel).all()]
