from sqlalchemy import Column, String, Integer, select
from .database import Base


class Files(Base):
    '''Class Files for Upload Files'''
    __tablename__ = "files"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String)
    onject_id = Column(String, unique=True)

    def get_all_files(object: object) -> bool:
        '''foo to check unique files in system for avoid duplicates '''
        return True if object not in select(Files).all() else False
