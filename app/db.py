import databases
import ormar
import sqlalchemy
import hashlib

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)


class Files(ormar.Model):

    class Meta(BaseMeta):
        tablename = "files"

    id: int = ormar.Integer(primary_key=True)
    filename: str = ormar.String(max_length=128, unique=True, nullable=False)
    hash_size: str = ormar.String(max_length=128, unique=True, nullable=False)
    path: str = ormar.String(max_length=128, unique=True, nullable=False)

    def get_hash(file: object) -> str:
        md = hashlib.md5()
        for chunk in iter(lambda: file.read(4096), b""):
            md.update(chunk)
        return md.hexdigest()


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
