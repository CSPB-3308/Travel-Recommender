from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)