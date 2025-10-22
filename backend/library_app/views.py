from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Author, Book, Borrowing, Genre


def index(request):
    books = Book.objects.filter(available=True).order_by("-id")[:3]
    return render(request, "index.html", {"books": books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    active_borrowing = Borrowing.objects.filter(
        book=book, returned_at__isnull=True
    ).exists()
    book.available = not active_borrowing
    return render(request, "book_detail.html", {"book": book})


def books_list(request):
    query = request.GET.get("q", "")
    genre_id = request.GET.get("genre", "")
    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query)
    if genre_id:
        books = books.filter(genre__id=genre_id.strip())
    paginator = Paginator(books.distinct().order_by("title"), 12)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    genres = Genre.objects.all().order_by("name")
    return render(
        request,
        "books.html",
        {
            "books": books,
            "genres": genres,
            "current_genre": genre_id,
            "query": query,
            "page_obj": page_obj,
        },
    )


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author, available=True)
    return render(
        request,
        "author_detail.html",
        {
            "author": author,
            "books": books,
        },
    )
