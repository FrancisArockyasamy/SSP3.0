
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import create_database, database_exists

# SQLAlchemy database setup
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/inventory"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


if(not database_exists(SQLALCHEMY_DATABASE_URL)):
    create_database(SQLALCHEMY_DATABASE_URL)