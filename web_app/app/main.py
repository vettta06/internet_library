from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse 
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Интернет-Библиотека")

base_dir = Path(__file__).resolve().parent 
templates = Jinja2Templates(directory=base_dir / "templates")


app.mount("/static", StaticFiles(directory=base_dir / ".." / "static"), name="static")

# костыль
fake_database = [
    {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": 1869},
    {"id": 2, "title": "Преступление и наказание", "author": "Федор Достоевский", "year": 1866},
    {"id": 3, "title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1967},
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": "Добро пожаловать в нашу библиотеку!"}
    )

@app.get("/books", response_class=HTMLResponse)
async def read_books(request: Request):
    return templates.TemplateResponse(
        "books.html",
        {"request": request, "books": fake_database}
    )

@app.get("/book/{book_id}", response_class=HTMLResponse)
async def read_book(request: Request, book_id: int):
    book = next((b for b in fake_database if b["id"] == book_id), None)
    if book is None:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    return templates.TemplateResponse("book.html", {"request": request, "book": book})

@app.get("/add-book", response_class=HTMLResponse)
async def add_book_form(request: Request):
    return templates.TemplateResponse("add_book.html", {"request": request})

@app.post("/add-book", response_class=HTMLResponse)
async def add_book(request: Request, title: str = Form(...), author: str = Form(...), year: int = Form(...)):
    print(f"Добавлена книга: {title}, {author}, {year}")  #заглушка
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/books", status_code=303)

@app.get("/404", response_class=HTMLResponse)
async def not_found(request: Request):
    return templates.TemplateResponse("404.html", {"request": request})