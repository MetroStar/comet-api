from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SqlAlchemy Setup
SQLALCHEMY_DATABASE_URL = 'sqlite:///./db.sqlite3'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
