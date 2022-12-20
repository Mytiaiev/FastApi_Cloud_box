import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker


DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSGRES_PASSWORD")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_NAME = os.environ.get("POSTGRES_DATABASE")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(engine)
