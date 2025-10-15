from django.contrib import admin
from .models import Author, Book, Borrowing


@admin.register(Author)
class AuthorAdmib(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'available')
    list_filter = ('available', 'year', 'genre')
    search_fields = ('title', 'author_name')


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'reader_name', 'borrowed_at', 'returned_at', 'is_returned')
    list_filter = ('returned_at', 'borrowed_at')
    search_fields = ('book__title', 'reader_name', 'reader_email')