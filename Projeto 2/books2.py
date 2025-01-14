from typing import Optional

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()     # uvicorn books2:app --reload


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)    # tornando o id opcional
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Gustavo Brito",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029
            }
        }
    }


BOOKS = [
    Book(1, 'Computer Science', 'Gustavo Brito', 'A very good book', 5, 2030),
    Book(2, 'Learning Django', 'codingwithroby', 'A excelent book', 5, 2025),
    Book(3, 'HP1', 'Author 1', 'Book Description', 1, 2028),
    Book(4, 'HP2', 'Author 2', 'Book Description', 2, 2030),
    Book(5, 'HP3', 'Author 3', 'Book Description', 4, 2020),
    Book(6, 'FastAPI', 'Author 4', 'Book Description', 8, 2015)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book-id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("books/")
async def create_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/publish/")
async def read_book_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


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


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
