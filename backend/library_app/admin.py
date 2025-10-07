from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmib(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'available')
    list_filter = ('available', 'year', 'genre')
    search_fields = ('title', 'author_name')