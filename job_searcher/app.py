from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount('/static', StaticFiles(directory='job_searcher/static'), name='static')
templates = Jinja2Templates(directory='job_searcher/templates')

from job_searcher.routes import home

