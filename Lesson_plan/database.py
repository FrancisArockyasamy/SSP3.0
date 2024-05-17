# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists,create_database

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/lesson_plan"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if(not database_exists(SQLALCHEMY_DATABASE_URL)):
    create_database(SQLALCHEMY_DATABASE_URL)