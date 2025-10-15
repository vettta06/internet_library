from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя автора")
    bio = models.TextField(blank=True, verbose_name="Биография")

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    year = models.IntegerField(verbose_name="Год издания")
    isbn = models.CharField(max_length=17, unique=True, verbose_name="ISBN")
    description = models.TextField(verbose_name="Описание")
    available = models.BooleanField(default=True, verbose_name="Доступна")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    reader_name = models.CharField(max_length=100, verbose_name="Имя читателя")
    reader_email = models.EmailField(verbose_name="Почта читателя")
    borrowed_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата выдачи")
    returned_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата возврата")

    @property
    def is_returned(self):
        return self.returned_at is not None
    
    def __str__(self):
        return f"{self.book.title} -> {self.reader_name}"
    
    class Meta:
        verbose_name = "Выдача книги"
        verbose_name_plural = "Выдача"