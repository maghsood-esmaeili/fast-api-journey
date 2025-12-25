from fastapi import APIRouter

router = APIRouter()

@router.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }

@router.get("/authors/{author_id}")
async def read_book(author_id: int):
    return {
        "book_id": "NewYork time best seller",
        "author": author_id
    } 

@router.get("/books")
async def read_book(book_id: int = None):
    if book_id:
        return {
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }
    else :
        return {
        "book_id": "All Books",
        "author": "F. Scott Fitzgerald"
    }