from django.shortcuts import render

from django.http import HttpResponse
from .models import testFlightData
from subprocess import run,PIPE
import sys
from pathlib import Path


def index(request):
    return render(request,'user_login/get_user.html')

def login(request):
    return render(request,'user_login/login.html')

def register(request):
    return render(request,'user_login/register.html')


def picker(request):
    return HttpResponse("These are the flights you found!")


def flights(request):
    return HttpResponse("These are the flights you found!")


def python_example(request):
    #This gets the relative path from this very views.py file!
    path = Path(__file__).parent / "python_example.py"
    #This is my input argument to python_example.py
    input1 = 'Date = 10/20/2020'
    #This runs an external python program and passes an input to it!
    out = run([sys.executable,path,input1],shell=False,stdout=PIPE)
    #This renders the output of the python program!
    return HttpResponse(out.stdout)
   
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
