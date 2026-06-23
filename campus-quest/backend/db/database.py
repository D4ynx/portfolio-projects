from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://postgres:password@localhost:5432/campus_quest"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
class Base(DeclarativeBase):
    pass