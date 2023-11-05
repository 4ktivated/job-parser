from fastapi import Depends, Form
from fastapi.responses import RedirectResponse
from tasks.all_parser.habr_vacancy import habr_jobs
from tasks.all_parser.hh_vacancy import hh_jobs_perm
from tasks.all_parser.big_corp import vk_jobs
from job_searcher.models import Vac
from sqlalchemy.orm import Session
from job_searcher.app import app, templates
from job_searcher.database.base import get_db, choose_db
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND
from sqlalchemy import create_engine


engine = create_engine("sqlite:///.\\job_searcher\\database\\DB\\vac.db")


def add():
    db_session = Session(bind=engine)

    try:
        for lang in ["python", "golang", "java"]:
            for i in hh_jobs_perm(lang):
                new_vac = Vac(
                    Title=i.get("Title"),
                    lang=i.get("lang"),
                    Company=i.get("Company"),
                    url=i.get("URL"),
                    Salary=i.get("Salary"),
                    Info=i.get("Info"),
                )
                db_session.add(new_vac)
            for i in habr_jobs(lang):
                new_vac = Vac(
                    Title=i.get("Title"),
                    lang=i.get("lang"),
                    Company=i.get("Company"),
                    url=i.get("URL"),
                    Salary=i.get("Salary"),
                    Info=i.get("Info"),
                )
                db_session.add(new_vac)
            for i in vk_jobs(lang):
                new_vac = Vac(
                    Title=i.get("Title"),
                    lang=i.get("lang"),
                    Company=i.get("Company"),
                    url=i.get("URL"),
                    Salary=i.get("Salary"),
                    Info=i.get("Info"),
                )
                db_session.add(new_vac)
        db_session.commit()
    except Exception as e:
        # Обработка возможных ошибок
        print("Ошибка при выполнении фоновой задачи:", str(e))
    finally:
        db_session.close()
        print(">>>>>>>>>>>>Vacancy add on DATA BASE")


def delete():
    db_session = Session(bind=engine)
    try:
        db_session.query(Vac).delete()
        db_session.commit()
    except Exception as e:
        # Обработка возможных ошибок
        print("Ошибка при выполнении фоновой задачи:", str(e))
    finally:
        db_session.close()
        print(">>>>>>>>>>>>DATA BASE is clear")
