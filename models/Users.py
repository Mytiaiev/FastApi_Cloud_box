from sqlalchemy import Column, String, Integer
from .database import Base


class Users(Base):
    '''Cass for Users models.'''
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    token = Column(String, unique=True)
