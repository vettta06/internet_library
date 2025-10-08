from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.filter(available=True).order_by('id')[:6]
    return render(request, 'index.html', {'books' : books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})