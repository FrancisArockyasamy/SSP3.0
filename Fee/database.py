import databases
import sqlalchemy
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
# Define the SQLAlchemy Base class
from sqlalchemy.ext.declarative import declarative_base

# Define the Base class using SQLAlchemy's declarative_base() function
Base = declarative_base()

# Replace DATABASE_URL with your actual database URL
DATABASE_URL = "postgresql://postgres:postgres@localhost/ssp_fees"

# Create a databases.Database object
database = databases.Database(DATABASE_URL)

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine(DATABASE_URL)

# Check if the database exists, if not, create it
if not database_exists(engine.url):
    create_database(engine.url)

# Create a sessionmaker object to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get the databases.Database object
def get_database() -> databases.Database:
    return database

# Function to get the SQLAlchemy engine
def get_engine() -> sqlalchemy.engine.base.Engine:
    return engine
