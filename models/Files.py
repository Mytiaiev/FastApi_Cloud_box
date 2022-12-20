from sqlalchemy import Column, String, Integer, select, crea
from .database import Base, async_session


class Files(Base):
    '''Class Files for Upload Files'''
    __tablename__ = "files"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String)
    object_id = Column(String, unique=True)

    def get_all_files(object: object) -> bool:
        '''foo to check unique files in system for avoid duplicates '''
        return True if object not in select(Files).all() else False

    def save_file(name: str, object: str) -> object:
        new_file = Files(name=name, object_id=object)
        return async_session.add(new_file)
