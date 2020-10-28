from django.shortcuts import render

from django.http import HttpResponse
from .models import testFlightData

def index(request):
    return HttpResponse("Hello, world welcome to the TravelRec Flights app")

def picker(request):
    return render(request,'flights/picker.html')
   
def flight_detail_view(request):
	obj = testFlightData.objects.get(flightNum='NK976')
	context ={
		'flightNum':obj.flightNum,
		'origin': obj.origin,
		'destination': obj.destination,
		'time': obj.flightDateTime,
		'flightCost': obj.flightCost
		}





	return render(request,'flights/detail.html',context)
# Create your views here.
