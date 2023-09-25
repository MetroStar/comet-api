from fastapi import FastAPI
from app.db import Base, engine
from app.spacecraft.router import router

# Create the app
app = FastAPI()
# Create database
Base.metadata.create_all(bind=engine)
# Add routes
app.include_router(router)
