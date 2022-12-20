from fastapi import FastAPI, File, UploadFile
from scheme import users
import models
from models import database, Files
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()
db = database.async_session()


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    if Files.get_all_files(file.file):
        try:
            with open(file.filename, 'wb') as f:
                while contents := file.file.read(300 * 104876):
                    f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            File.save_file(name=file.filename, object=file.file)
            file.file.close()
            return f'File {file.file} was upload successfully'
    else:
        return f'File {file.file} already in db'


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
