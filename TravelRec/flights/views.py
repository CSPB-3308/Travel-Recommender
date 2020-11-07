from django.shortcuts import render

from django.http import HttpResponse
from .models import testFlightData

def index(request):
    return render(request,'user_login/get_user.html')

def login(request):
    return render(request,'user_login/login.html')

def register(request):
    return render(request,'user_login/register.html')



def flights(request):
    return HttpResponse("These are the flights you found!")


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
