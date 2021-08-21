from django.db import models

# Create your models here.
class Homework(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=100)
    description = models.TextField()