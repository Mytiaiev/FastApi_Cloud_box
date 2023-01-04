import databases
import ormar
import sqlalchemy
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')


database = databases.Database(Settings().db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


settings = Settings()
engine = sqlalchemy.create_engine(Settings().db_url)
metadata.create_all(engine)
