from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from sqlalchemy_utils import create_database, database_exists

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/feedback"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL.replace("asyncpg", "psycopg2"))


if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
