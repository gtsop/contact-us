from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/message", response_model=schemas.Message)
def post_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.get('/messages', response_model=list[schemas.Message])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_messages(db=db, skip=skip, limit=limit)