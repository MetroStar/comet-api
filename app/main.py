from fastapi import FastAPI

from app.db import Base, engine
from app.health.router import router as health_router
from app.spacecraft.router import router as spacecraft_router

# Create the app
app = FastAPI()
# Create database
Base.metadata.create_all(bind=engine)
# Add routes
app.include_router(health_router)
app.include_router(spacecraft_router)
