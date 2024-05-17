from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

# Database connection
SQLALCHEMY_DATABASE_URL = "postgresql://root:Aero%400031@localhost/student_portal"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

if(not database_exists(SQLALCHEMY_DATABASE_URL)):
    create_database(SQLALCHEMY_DATABASE_URL)