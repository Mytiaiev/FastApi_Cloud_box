import ormar
import hashlib
import app.db


class Files(ormar.Model):

    class Meta(app.db.BaseMeta):
        tablename = "files"

    id: int = ormar.Integer(primary_key=True)
    filename: str = ormar.String(max_length=127, unique=True, nullable=False)
    hash_size: str = ormar.String(max_length=127, unique=True, nullable=False)
    path: str = ormar.String(max_length=127, unique=True, nullable=False)

    def get_hash(file: object) -> str:
        md = hashlib.md5()
        for chunk in iter(lambda: file.read(4095), b""):
            md.update(chunk)
        return md.hexdigest()
