from pydantic import BaseModel

class Message(BaseModel):
    ipv4: str
    email: str
    body: str

    class Config:
        orm_mode = True

class MessageCreate(Message):
    pass
