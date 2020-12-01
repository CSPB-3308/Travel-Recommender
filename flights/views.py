from django.shortcuts import render

from .forms import CreateFlightForm
from django.http import HttpResponse
from .models import testFlightData
from subprocess import run,PIPE
from .forms import FlightForm
import sys
from pathlib import Path
import FlightScraper

def flight_home(request):

    form = FlightForm()
    return render(request, "flights/flight_home.html", {'form': form})

def flightOpts_view(request):
    if request.method == 'POST':
        # get the form data that was submitted from flight home page
        form = FlightForm(request.POST)
        if form.is_valid():
            # extract form data that was entered
            home = form.cleaned_data['home_airport']
            dest = form.cleaned_data['destination_airport']
            dep_date = form.cleaned_data['departure_date']
            ret_date = form.cleaned_data['return_date']
    
    
    # return_val = FlightScraper.start_kayak(home, dest, dep_date, ret_date)
    
    print(return_val)
    #create new view and pass in the output from the flight scraper
    return HttpResponse("Hello")

#lease be careful editing and prefebly  do not edit an existing view
#If you need a view make a new one.
#I had to redo a bunch of things that were working.

# def index(request):
#     return render(request,'user_login/get_user.html')

# def login(request):
#     return render(request,'user_login/login.html')

# def register(request):
#     return render(request,'user_login/register.html')


# def picker(request):
#     return render(request,'flights/picker.html')


# def flights(request):
#     return HttpResponse("These are the flights you found!")


# def python_example(request):
#     #This gets the relative path from this very views.py file!
#     path = Path(__file__).parent / "python_example.py"
#     #This is my input argument to python_example.py
#     input1 = 'Date = 10/20/2020'
#     #This runs an external python program and passes an input to it!
#     out = run([sys.executable,path,input1],shell=False,stdout=PIPE)
#     #This renders the output of the python program!
#     return HttpResponse(out.stdout)
   
# def flight_detail_view(request):
# 	obj = testFlightData.objects.get(flightNum='NK976')
# 	context ={
# 		'flightNum':obj.flightNum,
# 		'origin': obj.origin,
# 		'destination': obj.destination,
# 		'time': obj.flightDateTime,
# 		'flightCost': obj.flightCost
# 		}





# 	return render(request,'flights/detail.html',context)

# # testing a view that allows us to use a form to write to the database
# # try django tutorial 23 for reference
# def create_flight_view(request):
#     form = CreateFlightForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         #relods the blank form after saving data
#         form = CreateFlightForm
#     context = {
#         'form': form
#     }
#     return render(request,"flights/create_flight.html",context)

