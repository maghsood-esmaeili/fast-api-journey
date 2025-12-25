from pydantic import BaseModel, Field


class Book(BaseModel):
    auther_id: int 
    title: str = Field(..., min_length=1, max_length=32)
    year: int 

class AllBook(BaseModel):
    author: str
    title: str 