from django.db import models



# Create your models for the flight app here.
# for now this is just a test setup to learn how to interact with a database... after we can link up to the data Becca/Bryant have generated
#In Django the class is the representation of a table in an SQL type language.. Django will take what we define here and format in the SQL type we define in the setings.py file (sqllite3)

class testFlightData(models.Model):
	flightNum = models.CharField(max_length = 10, primary_key = True)
	origin = models.CharField(max_length = 20)
	destination = models.CharField(max_length = 20)
	flightDateTime = models.DateTimeField()
	flightCost = models.DecimalField(max_digits = 5, decimal_places = 2)
	
		



