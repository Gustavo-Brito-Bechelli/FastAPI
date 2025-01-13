from fastapi import FastAPI

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
