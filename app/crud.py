from sqlalchemy.orm import Session
from . import models, schemas

def get_message(db: Session, id: int):
    return db.query(models.Message).filter(models.Message.id == id).first()

def get_message_by_email(db: Session, email: str):
    return db.query(models.Message).filter(models.Message.email == email).first()

def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Message).offset(skip).limit(limit).all()

def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(email=message.email, ipv4=message.ipv4, body=message.body)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message