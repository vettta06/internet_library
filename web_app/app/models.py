from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from .database import Base

class Librarian(Base):
    __tablename__ = "librarians"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(255))
    full_name = Column(String(100))


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    year = Column(Integer)
    isbn = Column(String(20), unique=True)
    quantity = Column(Integer, default=1)
    available = Column(Integer, default=1)


'''
class Reader(Base):
    __tablename__ = "readers"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100))
    phone = Column(String(20))
    address = Column(String(200))
    is_active = Column(Boolean, default=True)
    book_loans = relationship("BookLoan", back_populates="reader")



class BookLoan(Base):
    __tablename__ = "book_loans"    
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    reader_id = Column(Integer, ForeignKey("readers.id"))
    librarian_id = Column(Integer, ForeignKey("librarians.id"))
    loan_date = Column(DateTime, default=datetime.utcnow)
    expected_return_date = Column(DateTime)
    actual_return_date = Column(DateTime)
    status = Column(String(20), default="active")
    
    book = relationship("Book", back_populates="book_loans")
    reader = relationship("Reader", back_populates="book_loans")
    librarian = relationship("Librarian", back_populates="book_loans")
'''