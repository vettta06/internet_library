from django.contrib import admin

from .models import Author, Book, Borrowing, Genre


@admin.register(Author)
class AuthorAdmib(admin.ModelAdmin):
    """Класс для регистрации модели "Автор" в панели администратора."""

    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Класс для регистрации модели "Книга" в панели администратора."""

    list_display = ("title", "author", "year", "available")
    list_filter = ("available", "year", "genre")
    search_fields = ("title", "author__name")
    filter_horizontal = ("genre",)


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    """Класс для регистрации модели "Выдача книг" в панели администратора."""

    list_display = (
        "book", "reader_name", "borrowed_at", "returned_at", "is_returned"
    )
    list_filter = ("returned_at", "borrowed_at")
    search_fields = ("book__title", "reader_name", "reader_email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Класс для регистрации модели "Жанр" в панели администратора."""

    list_display = ("name",)
