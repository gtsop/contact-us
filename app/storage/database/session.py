from sqlalchemy.orm import sessionmaker
from .engine import engine

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
