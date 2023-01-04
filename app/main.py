from fastapi import FastAPI
from .settings.db_config import database, engine
from .settings.log_config import log_config
from endpoints import files, users
from models.users_db import metadata
from logging.config import dictConfig
import logging


logger = logging.getLogger('foo-logger')
dictConfig(log_config)


app = FastAPI(debug=True)


@app.on_event("startup")
async def startup() -> database.connect:
    """foo for connect to db
    """
    metadata.create_all(engine)
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown() -> database.disconnect:
    """foo for connect to db
    """
    if database.is_connected:
        await database.disconnect()


app.include_router(files.router)
app.include_router(users.router)
