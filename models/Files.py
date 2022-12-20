from sqlalchemy import Column, String, Integer, select
from fastapi_asyncalchemy.db.base import Base


class Files(Base):
    __tablename__ = "files"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String)
    etag = Column(String, unique=True)

    def get_all_files():
        return select(Files).all()
