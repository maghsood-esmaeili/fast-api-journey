import time
import asyncio
from fastapi import FastAPI
from pyexpat.errors import messages

app = FastAPI()

@app.get("/sync")
def simple_sync():
    time.sleep(2)
    return {
        "message": "sync api ..."
    }

@app.get("/async")
async def simple_async():
    await asyncio.sleep(2)
    return{
        "message": "async api ..."
    }