from sqlalchemy import Column, String, Integer, select
from fastapi_asyncalchemy.db.base import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    token = Column(String, unique=True)

    def get_all_users():
        return select(Users).all()
