from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from pathlib import Path

from .database import get_db, create_tables
from .models import Book, Librarian
from .auth import authenticate_user, get_password_hash

app = FastAPI(title="Интернет-Библиотека")

base_dir = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=base_dir / "templates")

def create_default_librarian(db: Session):
    if not db.query(Librarian).filter(Librarian.username == "admin").first():
        hashed_password = get_password_hash("admin123")
        librarian = Librarian(
            username="admin",
            password_hash=hashed_password,
            full_name="Администратор"
        )
        db.add(librarian)
        db.commit()
        print("Создан библиотекарь: admin / admin123")

@app.on_event("startup")
def on_startup():
    create_tables()
    db = next(get_db())
    create_default_librarian(db)

@app.get("/login")
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, username, password)
    if not user:
        return templates.TemplateResponse(
            "login.html", 
            {"request": request, "error": "Неверный логин или пароль"}
        )
    
    return RedirectResponse(url="/admin", status_code=303)

@app.get("/admin")
async def admin_dashboard(request: Request, db: Session = Depends(get_db)):
    books_count = db.query(Book).count()
    return templates.TemplateResponse(
        "admin_dashboard.html",
        {"request": request, "books_count": books_count}
    )

@app.get("/books")
async def books_list(request: Request, db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return templates.TemplateResponse(
        "books.html", 
        {"request": request, "books": books}
    )