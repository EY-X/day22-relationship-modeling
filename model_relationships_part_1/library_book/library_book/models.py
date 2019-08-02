from django.db import models

class Loan(models.Model):
    due_date = models.DateField(auto_now=False)
    renewed = models.DateField(auto_now=False)
class Hold(models.Model):
    date_placed = models.DateField(auto_now=False)


class Patron(models.Model):
    name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    email =  models.EmailField(max_length=254)
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
    hold_id = models.ForeignKey(Hold, on_delete=models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=255)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

