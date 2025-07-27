from fastapi import FastAPI
from app import models, database
from app.routes import router

app = FastAPI(title="KPA Form APIs")

models.Base.metadata.create_all(bind=database.engine)

app.include_router(router)
