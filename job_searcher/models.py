from attr import s
from sqlalchemy import Column, String, Integer, Text

from job_searcher.database.base import Base, choose_db, check_db


class Vac(Base):
    __tablename__ = 'vacs'

    id = Column(Integer, primary_key=True, index=True)
    lang = Column(String)
    title = Column(String)
    company = Column(String)
    url = Column(Text, nullable=True)
    salary = Column(String)
    info = Column(String)
    

Base.metadata.create_all(bind=choose_db(arg_db=check_db))
