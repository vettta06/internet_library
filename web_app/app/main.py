from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse 
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from pathlib import Path
from .database import get_db, create_tables
from .models import Book, Base


app = FastAPI(title="Интернет-Библиотека")

base_dir = Path(__file__).resolve().parent 
templates = Jinja2Templates(directory=base_dir / "templates")


app.mount("/static", StaticFiles(directory=base_dir / ".." / "static"), name="static")

@app.on_event("startup")
def on_startup():
    create_tables()
    print("Создание таблицы")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": "Добро пожаловать в нашу библиотеку!"}
    )


@app.get("/books", response_class=HTMLResponse)
async def read_books(request: Request, db: Session = Depends(get_db)):
    books = db.query(Book).all()
    books_data = []
    for book in books:
        books_data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year
        })
    
    return templates.TemplateResponse(
        "books.html",
        {"request": request, "books": books_data}
    )


@app.get("/book/{book_id}", response_class=HTMLResponse)
async def read_book(request: Request, book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    book_data = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "year": book.year
    }
    
    return templates.TemplateResponse("book.html", {"request": request, "book": book_data})


@app.get("/add-book", response_class=HTMLResponse)
async def add_book_form(request: Request):
    return templates.TemplateResponse("add_book.html", {"request": request})


@app.post("/add-book", response_class=HTMLResponse)
async def add_book(
    request: Request,
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    db: Session = Depends(get_db)
):
    new_book = Book(title=title, author=author, year=year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book) 
    
    print(f"Добавлена книга в БД: {title}, {author}, {year} (ID: {new_book.id})")
    
    return RedirectResponse(url="/books", status_code=303)

@app.get("/404", response_class=HTMLResponse)
async def not_found(request: Request):
    return templates.TemplateResponse("404.html", {"request": request})