from fastapi import FastAPI


app = FastAPI()  # uvicorn books:app --reload

BOOKS = [
    {'title': 'Title_one', 'author': 'Author_one', 'category': 'science'},
    {'title': 'Title_two', 'author': 'Author_two', 'category': 'science'},
    {'title': 'Title_three', 'author': 'Author_three', 'category': 'history'},
    {'title': 'Title_four', 'author': 'Author_four', 'category': 'math'},
    {'title': 'Title_five', 'author': 'Author_five', 'category': 'math'},
    {'title': 'Title_six', 'author': 'Author_two', 'category': 'portuguese'}
]


@app.get("/books")
async def read_all_books():  # url:127.0.0.1:8000/
    return BOOKS


# FastAPI le em ordem cronologica (de cima para baixo)
# @app.get("books/mybook")
# async def read_all_books():
#    return {'book_title': 'My favorite book'}


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book     # url: 127.0.0.1:8000/books/title_one
            # (caso utilize espaço na lista) url: 127.0.0.1:8000/books/title%20one ("%20" == espaço)


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author: str, category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return
