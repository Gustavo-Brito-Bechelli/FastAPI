from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()     # uvicorn books2:app --reload


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int


BOOKS = [
    Book(1, 'Computer Science', 'Gustavo Brito', 'A very good book', 5),
    Book(2, 'Learning Django', 'codingwithroby', 'A excelent book', 5),
    Book(3, 'HP1', 'Author 1', 'Book Description', 1),
    Book(4, 'HP2', 'Author 2', 'Book Description', 2),
    Book(5, 'HP3', 'Author 3', 'Book Description', 4),
    Book(6, 'FastAPI', 'Author 4', 'Book Description', 8)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())  # Book(**book_request.dict()) == converter a requesição para Book objeto
    # Book(**book_request.model_dump()) == caso o ".dict()" esteja dando erro
    BOOKS.append(new_book)
