from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    

class Order(models.Model):
    order_number = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)