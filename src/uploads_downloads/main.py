import shutil
from fastapi import UploadFile, FastAPI, File

app = FastAPI()

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    with open (f"upload/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename}