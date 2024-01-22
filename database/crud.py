from sqlalchemy.orm import Session

from . import schemas, models



def get_vacs_by_lang(db: Session, lang: str):
    return db.query(models.Vac).filter(models.Vac.lang == lang).all()

def get_vacs(db: Session):
    return db.query(models.Vac).all()

def clear_vacs(db: Session):
    db.query(models.Vac).delete()
    db.commit()

def create_vacs(db: Session, handlers: list[schemas.VacCreate], text:str):
    # text_list = ["python", "golang", "java", "php"]
    for func in handlers:
        # for lang in text_list:
        for vacaincie in func(text):
            new_vac = models.Vac(
                title=vacaincie['Title'],
                lang=vacaincie['lang'],
                company=vacaincie['Company'],
                url=vacaincie['URL'],
                salary=vacaincie['Salary'],
                info=vacaincie['Info'],
            )
            db.add(new_vac)    
            db.commit()
            db.refresh(new_vac)


