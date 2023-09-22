from fastapi import FastAPI
from app.spacecraft.router import router

# Create the app
app = FastAPI()
# Add routes
app.include_router(router)
