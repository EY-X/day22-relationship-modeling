from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Residence(models.Model):
    address = models.CharField(max_length=255)
    year_founded = models.DateField(auto_now_add=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.DateField(auto_now_add=True)
    residence_id = models.ForeignKey(Residence, on_delete=models.CASCADE)

class Province(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.DateField(auto_now_add=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

class Country(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.DateField(auto_now_add=True)
    national_animal = models.CharField(max_length=255)
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE)







