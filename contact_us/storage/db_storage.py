from sqlalchemy import Column, String
from contact_us.message import Message
from .database import BaseModel, Session, engine
from .storage import Storage

class MessageModel(BaseModel):
    __tablename__ = "messages"

    email = Column(String, primary_key=True, index=True)
    body = Column(String)

BaseModel.metadata.create_all(bind=engine)

class DBStorage(Storage):
    def __init__(self):
        self.db = Session()
    
    def __del__(self):
        self.db.close()

    def append(self, message: Message):
        db_message = MessageModel(email=message.email, body=message.body)
        self.db.add(db_message)
        self.db.commit()
        self.db.refresh(db_message)
        return db_message
    
    def all(self):
        return [
            Message(email=entry.email, body=entry.body) for entry in self.db.query(MessageModel).all()
            ]
