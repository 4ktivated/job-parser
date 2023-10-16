from sqlalchemy import Column, String, Integer, Text

from job_searcher.database.base import Base, choose_db, check_db


class Vac(Base):
    __tablename__ = 'vacs'

    id = Column(Integer, primary_key=True, index=True)
    lang = Column(String)
    Title = Column(String)
    Company = Column(String)
    url = Column(Text, nullable=True, unique=True)
    Salary = Column(String)
    Info = Column(String)
    

Base.metadata.create_all(bind=choose_db(arg_db=check_db))
