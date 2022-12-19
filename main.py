from fastapi import FastAPI, File, UploadFile
from os import getcwd
from fastapi.responses import FileResponse

app = FastAPI()


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
