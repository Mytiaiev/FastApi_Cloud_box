from fastapi import FastAPI, File, UploadFile
from app.db import User, database, Files


app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    """root page

    Returns:
        dict: return objects from Files as dict
    """
    return await Files.objects.get_or_none()


@app.on_event("startup")
async def startup() -> database.connect:
    """foo for connect to db
    """
    if not database.is_connected:
        await database.connect()
    await User.objects.get_or_create(username="test")


@app.on_event("shutdown")
async def shutdown() -> database.disconnect:
    """foo for connect to db
    """
    if database.is_connected:
        await database.disconnect()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if Files.get_all_files(file.file):
        try:
            with open(file.filename, 'wb') as f:
                while contents := file.file.read(300 * 104876):
                    f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            await Files.save_file(name=file.filename, object=file.file)
            file.file.close()
            return f'File {file.file} was upload successfully'
    else:
        return f'File {file.file} already in db'
