from django.db import models

class Chapter(models.Model):
    title = models.CharField(max_length=255)


class Book(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    chapter_id = models.ForeignKey(Chapter, on_delete=models.CASCADE)

class Reader(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)

class Author(models.Model):
    name = models.CharField(max_length=255)

class AuthorBook(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

class BookReader(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader_id = models.ForeignKey(Reader, on_delete=models.CASCADE)





