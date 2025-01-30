from fastapi import APIRouter,status
from fastapi.exceptions import HTTPException

from typing import List
from src.books.book_data import books
from src.books.schemas import Book,UpdateBook




book_router = APIRouter()

@book_router.get('/', response_model=List[Book])
async def get_books():
    return books

@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    book_dict = book.model_dump()   # make model dictionary
    books.book_routerend(book_dict)
    return book_dict

@book_router.get('/{book_id}')
async def get_a_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="The book is not found")

@book_router.patch('/{book_id}')
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

@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Books not found for this ID")
