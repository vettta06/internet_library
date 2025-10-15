from django.shortcuts import render
from .models import Book, Genre


def index(request):
    books = Book.objects.filter(available=True).order_by('-id')[:3]
    return render(request, 'index.html', {'books': books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})


def books_list(request):
    query = request.GET.get('q', '')
    genre_id = request.GET.get('genre', '')
    books = Book.objects.filter(available=True)
    if query:
        books = books.filter(title__icontains=query)
    if genre_id:
        books = books.filter(genre__id=genre_id.strip())
    books = books.distinct().order_by('title')
    genres = Genre.objects.all().order_by('name')
    return render(request, 'books.html', {
        'books': books,
        'genres': genres,
        'current_genre': genre_id,
        'query': query,
    })
