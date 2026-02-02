from fastapi import FastAPI
from api.v1.routers import router

app = FastAPI()
app.include_router(router)
