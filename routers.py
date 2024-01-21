from fastapi.params import Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from database.crud import create_vac, get_vacs_by_lang, get_vacs
from database.models import Vac
from starlette.status import HTTP_303_SEE_OTHER



from database.base_params import get_db

from tasks.habr_vacancy import habr_jobs
from tasks.hh_vacancy import hh_jobs_perm
from tasks.geekjob import geekjob_jobs


templates = Jinja2Templates(directory="templates")
text_list = ["python", "golang", "java", "php"]
func_list = [hh_jobs_perm, habr_jobs, geekjob_jobs]

router = APIRouter()


@router.get("/")
def home(request: Request, db_session: Session = Depends(get_db)):
    vacs = get_vacs(db_session, limit=1000)
    return templates.TemplateResponse('job/index.html',
                                      {'request': request,
                                       'vac_list': vacs,
                                       'text_list': text_list}
                                      )

@router.get('/{lang}')
def chose_lang(lang: str, request: Request, db_session: Session = Depends(get_db)):
    vacs = get_vacs_by_lang(db_session , lang)
    return templates.TemplateResponse('job/index.html',
                                      {'request': request,
                                       'vac_list': vacs,
                                       'text_list': text_list}
                                      )


#del and add action

@router.post("/add/{yap}")
async def add(yap: str ,db_session: Session = Depends(get_db)):
    create_vac(db_session, func_list, yap)
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

@router.get("/del")
async def delete(db_session: Session = Depends(get_db)):
    db_session.query(Vac).delete()
    db_session.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)



