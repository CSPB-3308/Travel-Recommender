from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Destination(models.Model):
   name = models.CharField(max_length=200)
   country = models.CharField(max_length=200,default="USA")
   description = models.CharField(max_length=200,default="rocks and water")

   def __str__(self):
      return self.name

class Lodging(models.Model):
   name = models.CharField(max_length=200)
   destinationID = models.ForeignKey(Destination,null=True,on_delete=models.SET_NULL)
   address = models.CharField(max_length=200)
   star_rating = models.DecimalField(max_digits=5, decimal_places=2)
   description = models.CharField(max_length=200)

   def __str__(self):
      return self.name

#class Destination(models.Model):
#   name= models.CharField(max_length=200) 
#
#   def __str__(self):
#      return self.name

#class Item(models.Model):
#   destination = models.ForeignKey(Destination,default=1, #on_delete=models.SET_DEFAULT)
#   state = models.CharField(max_length=300)
#   country = models.CharField(max_length=300)
#   description = models.CharField(max_length=300)
#
#   def __str__(self):
#      return self.description
