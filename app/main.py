from fastapi import FastAPI
from app.db import database
from routers import files, users


app = FastAPI()


@app.on_event("startup")
async def startup() -> database.connect:
    """foo for connect to db
    """
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
