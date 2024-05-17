
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Extract database connection parameters from DATABASE_URL
db_params = DATABASE_URL.split('/')
db_name = db_params[-1]
db_url_without_dbname = '/'.join(db_params[:-1])

# Create a connection to the PostgreSQL server without specifying a database
conn = psycopg2.connect(db_url_without_dbname)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

# Create database if it doesn't exist
cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}'")
exists = cur.fetchone()
if not exists:
    cur.execute(f"CREATE DATABASE {db_name}")

cur.close()
conn.close()

# Now connect to the newly created or existing database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
