from fastapi import FastAPI, File, UploadFile
from app.db import database
from models import files, users


app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    """root page

    Returns:
        dict: return objects from Files as dict
    """
    return await files.Files.objects.get_or_none()


@app.on_event("startup")
async def startup() -> database.connect:
    """foo for connect to db
    """
    if not database.is_connected:
        await database.connect()
    await users.User.objects.get_or_create(username="test")


@app.on_event("shutdown")
async def shutdown() -> database.disconnect:
    """foo for connect to db
    """
    if database.is_connected:
        await database.disconnect()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if files.Files.objects.filter(
            hash_size=files.Files.get_hash(file.file)).exists():
        return f'File {file.file} already in db'
    else:
        try:
            with open(file.filename, 'wb') as f:
                while contents := file.file.read(300 * 104876):
                    f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            path = f'{file.filename}.{file.content_type}'
            await files.Files.objects.create(
                filename=str(file.filename),
                hash_size=files.Files.get_hash(file.file),
                path=path)
            file.file.close()
            return f'File {file.file} was upload successfully'
