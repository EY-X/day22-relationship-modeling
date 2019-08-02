from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()


class Viewer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class FilmViewer(models.Model):
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    viewer_id = models.ForeignKey(Viewer, on_delete=models.CASCADE)

