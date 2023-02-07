from typing import Type, Tuple, Callable
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, Mapped, mapped_column, sessionmaker

from contact_us.settings import settings
from contact_us.app.message import Message

from .database import BaseModel
from .storage import Storage


def session_factory() -> Tuple[Session, Engine]:
    engine = create_engine(
        # settings.storage_db_uri, connect_args={"check_same_thread": False}
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
    )
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session(), engine


class MessageModel(BaseModel):
    __tablename__ = "messages"

    email: Mapped[str] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column()
    is_sent: Mapped[bool] = mapped_column(nullable=False)


class DBStorage(Storage):
    def __init__(
        self, create_session: Callable[[], Tuple[Session, Engine]] = session_factory
    ):
        self.db, self.engine = create_session()
        BaseModel.metadata.create_all(bind=self.engine)

    def __del__(self):
        self.db.close()

    def append(self, message: Message):
        db_message = MessageModel(
            email=message.email, body=message.body, is_sent=message.is_sent
        )
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
        return [
            Message(email=entry.email, body=entry.body, is_sent=entry.is_sent)
            for entry in self.db.query(MessageModel).all()
        ]
