import json

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError

from starlette.responses import JSONResponse
import book_router
from models import Book, AllBook

app = FastAPI()

app.include_router(book_router.router)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exec):
    return JSONResponse(
        status_code=exec.status_code,
        content={
            "message": "Oops! Something went wrong"
        }
    )
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(
            "This is a plain text response:"
            f"\n {json.dumps(exc.errors(), indent=2)}",
             status_code=status.HTTP_400_BAD_REQUEST
    )

@app.get("/raise-exception")
async def raise_exception():
    raise HTTPException(status_code=500)

@app.post("/books")
async def create_book(book: Book):
    return book

@app.get("/allbookstore")
async def get_all_books() -> list[AllBook]:
    return [{
        # "id": 1,
        "author": "maghsood",
        "title": "be successful in jsut 3 month"
    }]