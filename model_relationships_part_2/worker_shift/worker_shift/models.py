from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=255)
    wage = models.CharField(max_length=255)

class Shift(models.Model):
    day = models.DateField(auto_now=False)
    age = models.IntegerField()

class WorkerShift(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE)