from pydantic import BaseModel


class VacBase(BaseModel):
    lang: str
    title: str
    company: str
    url: str
    salary: str
    info: str



class VacCreate(VacBase):
    lang: str
    Title: str
    Company: str
    URL: str
    Salary: str
    Info: str



class Vac(VacBase):
    vac_id: int

    class Config:
        from_attributes = True