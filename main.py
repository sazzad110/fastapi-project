from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "publisher": "Addison-Wesley", "published_date": "1999-10-20", "page_count": 352, "language": "English"},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin", "publisher": "Prentice Hall", "published_date": "2008-08-11", "page_count": 464, "language": "English"},
    {"id": 3, "title": "You Don't Know JS", "author": "Kyle Simpson", "publisher": "O'Reilly Media", "published_date": "2014-12-27", "page_count": 278, "language": "English"},
    {"id": 4, "title": "Introduction to the Theory of Computation", "author": "Michael Sipser", "publisher": "Cengage Learning", "published_date": "2012-06-27", "page_count": 504, "language": "English"},
    {"id": 5, "title": "Design Patterns", "author": "Erich Gamma", "publisher": "Addison-Wesley", "published_date": "1994-10-21", "page_count": 416, "language": "English"},
    {"id": 6, "title": "Eloquent JavaScript", "author": "Marijn Haverbeke", "publisher": "No Starch Press", "published_date": "2018-12-04", "page_count": 472, "language": "English"},
    {"id": 7, "title": "Python Crash Course", "author": "Eric Matthes", "publisher": "No Starch Press", "published_date": "2015-11-01", "page_count": 560, "language": "English"},
    {"id": 8, "title": "The Art of Computer Programming", "author": "Donald Knuth", "publisher": "Addison-Wesley", "published_date": "1968-01-01", "page_count": 672, "language": "English"},
    {"id": 9, "title": "JavaScript: The Good Parts", "author": "Douglas Crockford", "publisher": "O'Reilly Media", "published_date": "2008-05-15", "page_count": 176, "language": "English"},
    {"id": 10, "title": "Effective Java", "author": "Joshua Bloch", "publisher": "Addison-Wesley", "published_date": "2017-12-27", "page_count": 416, "language": "English"},
]

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
class UpdateBook(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

@app.get('/books', response_model=List[Book])
async def get_books():
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    book_dict = book.model_dump()   # make model dictionary
    books.append(book_dict)
    return book_dict

@app.get('/books/{book_id}')
async def get_a_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="The book is not found")

@app.patch('/books/{book_id}')
async def update_a_book(book_id:int,update_book: UpdateBook) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = update_book.title
            book['author'] = update_book.author
            book['publisher'] = update_book.publisher
            book['page_count'] = update_book.page_count
            book['language'] = update_book.language
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book is not found for update")

@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Books not found for this ID")
