from fastapi import FastAPI
from app.spacecraft.router import router

app = FastAPI()
app.include_router(router)
