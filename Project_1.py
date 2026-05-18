# An API to get books
from fastapi import FastAPI,Body

#imports
app=FastAPI()
BOOKS=[{"title":"BOOK1", "author":"AUTHOR1", "category":"SCIENCE"},
       {"title":"BOOK2", "author":"AUTHOR2", "category":"SCIENCE"},
       {"title":"BOOK3", "author":"AUTHOR3", "category":"HISTORY"}
       ,{"title":"BOOK4", "author":"AUTHOR5", "category":"MATH"},
       {"title":"BOOK5", "author":"AUTHOR5", "category":"MATH"},
       {"title":"BOOK6", "author":"AUTHOR2", "category":"HISTORY"}]

#getallbooks
@app.get("/books")
async def get_books():
    return BOOKS
#get book by title
@app.get("/books/by_title/{title}")
async def get_books(title:str):
    for book in BOOKS:
        if(book.get("title").lower()==title.lower()):
            return book
#get book by category
@app.get("/books/by_category")
async def get_book_category(book_category:str):
    books_to_return=[]
    for book in BOOKS:
        if(book.get("category").lower()==book_category.lower()):
            books_to_return.append(book)
    return books_to_return
#get all books by a specific author
@app.get("/books/byauthor/{author}")
async def get_books_category(author1:str):
    books_to_return=[]
    for book in BOOKS:
        if(book.get("author").lower()==author1.lower()):
            books_to_return.append(book)
    return books_to_return
#create book
@app.post("/books/add_book")
async def add_book(newbook=Body()):
    BOOKS.append(newbook)
#update book
@app.put("/books/update_book")
async def update_book(newbook=Body()):
    for i in range(0,len(BOOKS)):
        if(BOOKS[i].get("title").lower()==newbook.get("title").lower()):
            BOOKS[i]=newbook
#delete book
@app.delete("/books/delete_book/{title}")
async def delete_book(title:str):
    for i in range(0,len(BOOKS)):
        if(BOOKS[i].get("title").lower()==title.lower()):
            BOOKS.pop(i)
            break
