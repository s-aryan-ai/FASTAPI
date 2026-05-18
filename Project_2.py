from typing import Optional
from fastapi import FastAPI,Body, Path, Query
from pydantic import BaseModel,Field
app=FastAPI()
class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int
    publish_year:int
    def __init__(self, id,title,author,description,rating,publish_year):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.publish_year=publish_year
class BookRequest(BaseModel):
    id: Optional[int]=None
    title: str=Field(min_length=3, max_length=30)
    author: str=Field(min_length=3, max_length=40)
    description: str=Field(min_length=4, max_length=100)
    rating: int=Field(gt=0, lt=6)
    publish_year: int=Field(gt=1900,lt=2027)
    class Config:
        schema_extra={
            "example":{
                "id":2,
                "title":"Title1",
                "author":"Author1",
                "description":"Description1",
                "rating":1,
                "publish_year":1999
            }
        }
BOOKS=[Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)]

@app.get("/books")
async def get_books():
    return BOOKS
@app.get("/books")
async def get_books():
    return BOOKS

@app.get("/book/{publish_date}")
async def get_book_by_publish_date(publish_date:int):
    books_to_return=[]
    for book in BOOKS:
        if book.publish_date==publish_date:
            books_to_return.append(book)
    return books_to_return
@app.post("/books/add_book")
async def add_book(book:BookRequest):
    newbook=Book(**book.model_dump())
    BOOKS.append(find_id(newbook))

def find_id(book:Book):
    if len(BOOKS)==0:
        book.id=1
    else:
        book.id=BOOKS[-1].id+1
    return book

@app.get("/books/get_book_by_id/{book_id}")
async def get_book_by_id(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            return book
@app.get("/books/get_book_by_rating/{rating}")
async def get_book_by_id(rating:int=Path(gt=0,lt=6)):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==rating:
            books_to_return.append(book)
    return books_to_return

@app.put("/books/update_book")
async def update_book(bookrequest:BookRequest):
    for i in range(0,len(BOOKS)):
        if BOOKS[i].id==bookrequest.id:
            newBook=Book(**bookrequest.model_dump())
            BOOKS[i]=newBook


@app.delete("/books/delete_book/{book_id}")
async def delete_book(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            BOOKS.remove(book)
