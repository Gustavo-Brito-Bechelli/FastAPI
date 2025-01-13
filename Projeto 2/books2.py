from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

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
    id: Optional[int] = Field(description='ID is not needed on create', default=None)    # tornando o id opcional
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Gustavo Brito",
                "description": "A new description of a book",
                "rating": 5
            }
        }
    }


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
    BOOKS.append(find_book_id(new_book))


# mudando o ID para o proximo depois do ultimo da lista
def find_book_id(book: Book):

    # Jeito 1
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    # Jeito 2
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1

    return book
