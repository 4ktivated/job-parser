from fastapi import APIRouter, FastAPI

from database import models

from database.base_params import  check_db
from routers import router

app = FastAPI(
    title="Job searcher"
    )
app.include_router(router)
models.Base.metadata.create_all(bind=check_db)


