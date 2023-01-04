from fastapi import APIRouter, File, UploadFile
from app.settings.db_config import database
from models import files
import aiofiles


router = APIRouter()


@router.get("/")
async def read_root() -> dict:
    """root page

    Returns:
        dict: return objects from Files as dict
    """
    return await files.Files.objects.all()


@router.on_event("startup")
async def startup() -> database.connect:
    """foo for connect to db
    """
    if not database.is_connected:
        await database.connect()


@router.on_event("shutdown")
async def shutdown() -> database.disconnect:
    """foo for connect to db
    """
    if database.is_connected:
        await database.disconnect()


@router.post("/upload")
async def upload(file: UploadFile = File(...)) -> UploadFile:
    uploads_hash = files.Files.get_hash(file.file)
    if await files.Files.objects.filter(hash_size=uploads_hash).exists():
        return f'File {file.file} already in db'
    else:
        try:
            async with aiofiles.open(file.filename, 'wb') as out_file:
                content = await file.read()
                await out_file.write(content)
            return {"info": f"file '{file.filename}' saved"}
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            await files.Files.objects.create(
                filename=str(file.filename),
                hash_size=uploads_hash,
                path=file.filename)
            file.file.close()
            return f'File {file.file} was upload successfully'
