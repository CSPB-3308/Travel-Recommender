from django.db import models


# Create your models here.
class ToDoTable(models.Model):
    name = models.CharField(max_length=200)
    typeplace = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    about = models.TextField()

