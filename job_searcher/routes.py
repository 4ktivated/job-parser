from fastapi import Request, Depends, Form, BackgroundTasks
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND
from tasks.all_parser.habr_vacancy import habr_jobs
from tasks.all_parser.hh_vacancy import hh_jobs_perm
from tasks.all_parser.big_corp import vk_jobs
from tasks.all_parser.all_in_one import add, delete
from apscheduler.schedulers.background import BackgroundScheduler

from job_searcher.config import settings
from job_searcher.database.base import get_db
from job_searcher.app import app, templates
from job_searcher.models import Vac

from time import sleep


bg_scheduler = BackgroundScheduler()
#bg_scheduler.add_job(add, 'interval', hours=6)
bg_scheduler.add_job(add, 'interval', seconds=28803)
#bg_scheduler.add_job(delete, 'interval', hours=20)
bg_scheduler.add_job(delete, 'interval', seconds=57600)
bg_scheduler.start()

@app.on_event("shutdown")
async def shutdown_event():
    bg_scheduler.shutdown()



text_list = ['python', 'golang', 'java']
@app.get('/')
def home(request: Request, db_session: Session = Depends(get_db)):
    vacs = db_session.query(Vac).all()
    return templates.TemplateResponse('job/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'vac_list': vacs,
                                       'text_list': text_list
                                        }
                                      )

@app.get('/python')
def python(request: Request, db_session: Session = Depends(get_db)):
    vacs = db_session.query(Vac).filter(Vac.lang == 'python')
    return templates.TemplateResponse('job/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'vac_list': vacs,
                                       'text_list': text_list}
                                      )

@app.get('/golang')
def python(request: Request, db_session: Session = Depends(get_db)):
    vacs = db_session.query(Vac).filter(Vac.lang == 'golang')
    return templates.TemplateResponse('job/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'vac_list': vacs,
                                       'text_list': text_list}
                                      )
    
@app.get('/java')
def python(request: Request, db_session: Session = Depends(get_db)):
    vacs = db_session.query(Vac).filter(Vac.lang == 'java')
    return templates.TemplateResponse('job/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'vac_list': vacs,
                                       'text_list': text_list}
                                      )
    
    


#ЭТОТ СЕГМЕНТ СЕЙЧАС НЕ СИЛЬНО АТУАЛЕН РАЗВЕ ЧТО ДЛЯ РУЧНОЙ РАБОЫТ С БД
@app.post('/add')
def addon(lang: str = Form(), db_session: Session = Depends(get_db)):
    for i in hh_jobs_perm(lang):
        new_vac = Vac(Title = i.get('Title'),
                      lang = i.get('lang'),
                       Company = i.get('Company'),
                       url = i.get('URL'),
                       Salary = i.get('Salary'),
                       Info = i.get('Info'))
        db_session.add(new_vac)
    for i in habr_jobs(lang):
        new_vac = Vac(Title = i.get('Title'),
                      lang = i.get('lang'),
                       Company = i.get('Company'),
                       url = i.get('URL'),
                       Salary = i.get('Salary'),
                       Info = i.get('Info'))
        db_session.add(new_vac)
    for i in vk_jobs(lang):
        new_vac = Vac(Title = i.get('Title'),
                      lang = i.get('lang'),
                       Company = i.get('Company'),
                       url = i.get('URL'),
                       Salary = i.get('Salary'),
                       Info = i.get('Info'))
        db_session.add(new_vac)
    db_session.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)

@app.delete('/delete')
def deleted(db_session: Session = Depends(get_db)):
    db_session.query(Vac).delete()
    db_session.commit()


    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)



