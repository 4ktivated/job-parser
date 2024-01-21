from curses import meta
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

url = os.getenv('SQLALCHEMY_DATABASE_URL')
metadata = MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def choose_db(arg_db):
    engine = create_engine(url, echo=True)
    return engine


check_db = choose_db(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=check_db)
Base = declarative_base()