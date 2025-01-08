from fastapi import FastAPI


app = FastAPI()  # uvicorn books:app --reload

BOOKS = [
    {'title': 'Title_one', 'author': 'Author_one', 'category': 'science'},
    {'title': 'Title_two', 'author': 'Author_two', 'category': 'science'},
    {'title': 'Title_three', 'author': 'Author_three', 'category': 'history'},
    {'title': 'Title_four', 'author': 'Author_four', 'category': 'math'},
    {'title': 'Title_five', 'author': 'Author_five', 'category': 'math'},
    {'title': 'Title_six', 'author': 'Author_six', 'category': 'portuguese'}
]


@app.get("/books")
async def read_all_books():  # url:127.0.0.1:8000/api-endpoint
    return BOOKS

