from fastapi import FastAPI

from app.admin.router import router as admin_router
from app.applicants.router import router as applicants_router
from app.cases.router import router as cases_router
from app.db import Base, engine
from app.health.router import router as health_router
from app.users.router import router as users_router

# Create the app
app = FastAPI()
# Create database
Base.metadata.create_all(bind=engine)
# Add routes
app.include_router(cases_router)
app.include_router(applicants_router)
app.include_router(users_router)
app.include_router(admin_router)
app.include_router(health_router)
