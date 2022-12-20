from fastapi import FastAPI, File, UploadFile
from os import getcwd
from scheme import users
import models
from models import database, Users, async_session
from fastapi.responses import FileResponse
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()
db = async_session()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.post("/files/")
async def create_file(file: bytes = File()):
    if len(file) >= 300*1048576:
        return {"Your file is more than 300MB"}
    return {'filename': file.filename, "file_size": len(file)}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return FileResponse(path=getcwd() + "/" + file.filename,
                        media_type='application/octet-stream',
                        filename=file.filename)


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = db.query(models.Users).all()
    if not user_dict:
        raise HTTPException(status_code=400,
                            detail="Incorrect username or password")
    user = users.UserInDB(**user_dict)
    hashed_password = users.fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400,
                            detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: users.User = Depends(
        users.get_current_active_user)):
    return current_user
