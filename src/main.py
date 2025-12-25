from fastapi import FastAPI
import project_router

app = FastAPI()

app.include_router(project_router.router)


@app.get("/")
def greeting():
    return {"Hello": "World"}
