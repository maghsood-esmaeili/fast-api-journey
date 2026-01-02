import shutil
from fastapi import UploadFile, FastAPI, File
from fastapi.responses import FileResponse


app = FastAPI()

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    with open (f"upload/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename}

@app.get("/download/{filename}", response_class=FileResponse)
async def download_file(filename: str):
    # first check file does exist or not
    return FileResponse(f"upload/{filename}", filename=filename)
