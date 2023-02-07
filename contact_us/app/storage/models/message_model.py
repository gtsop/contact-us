from sqlalchemy.orm import  Mapped, mapped_column 
from contact_us.app.message import Message
from .base_model import BaseModel

class MessageModel(BaseModel):
    __tablename__ = "messages"

    email: Mapped[str] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column()
    is_sent: Mapped[bool] = mapped_column(nullable=False)


    @staticmethod
    def from_message(message: Message) -> 'MessageModel':
        return MessageModel(email=message.email, body=message.body, is_sent=message.is_sent)
    
    def to_message(self):
        return Message(email=self.email, body=self.body, is_sent=self.is_sent)
    