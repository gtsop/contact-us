from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class MessageIn(BaseModel):
    email: EmailStr
    message: str

@app.post("/message")
def post_message(input: MessageIn) -> MessageIn:
    return input
