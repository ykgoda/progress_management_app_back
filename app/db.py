from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@0.0.0.0:5432/progress_management_app_back"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def validate_database():
    if not database_exists(engine.url):
        create_database(engine.url)
