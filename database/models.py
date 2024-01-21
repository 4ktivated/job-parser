from sqlalchemy import Column, String, Integer, Text
from database.base_params import Base


class Vac(Base):
    __tablename__ = "vacs"

    id = Column(Integer, primary_key=True, index=True)
    lang = Column(String)
    title = Column(String)
    company = Column(String)
    url = Column(Text, nullable=True)
    salary = Column(String)
    info = Column(String)
