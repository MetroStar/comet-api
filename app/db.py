from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SqlAlchemy Setup
engine = create_engine(settings.DB_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
