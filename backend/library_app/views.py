from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.filter(available=True).order_by('-id')[:3]
    return render(request, 'index.html', {'books': books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})


def books_list(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(
            available = True,
            title__icontains=query
        ).order_by('title')
    else:
        books = Book.objects.filter(available=True).order_by('title')
    return render(request, 'books.html', {'books': books, 'query': query})