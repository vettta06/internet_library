from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("books/", views.books_list, name="books_list"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
    path("autocomplete/", views.autocomplete, name="autocomplete"),
]
