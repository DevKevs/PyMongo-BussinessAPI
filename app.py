from fastapi import FastAPI
from routes.bussines import bussines

app = FastAPI(
    title="Bussines Rest API with MongDB",
    version="0.0.1"
)
app.include_router(bussines)