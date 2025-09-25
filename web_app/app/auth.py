from passlib.context import CryptContext
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .models import Librarian


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(Librarian).filter(Librarian.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user
