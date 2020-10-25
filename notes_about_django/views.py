from django.shortcuts import render
from django.http import HttpResponse

from .models import Destination
from .models import Lodging

import requests
import os

# Create your views here.
#def index(request):
#    times = int(os.environ.get('TIMES',3))
#    return HttpResponse('Hello! ' * times)

def index(request):
    return render(request,"travel_recommender.html")

def working(request):
    place = Destination.objects.get(id=3)
    hotel = Lodging.objects.get(id=2)
    return render(request,"base.html",{"city":place,"city_description": place.description,"hotel":hotel.name,"rating":hotel.star_rating})


#def index(request):
#    r = requests.get('http://httpbin.org/status/418')
#    print(r.text)
#    return HttpResponse('<pre>' + r.text + '</pre>')

#def index(request):
#    # return HttpResponse('Hello from Python!')
#    return render(request, "index.html")

def best_airports(request):
   return render(request,"best_airports.html")


def itinerary(request):
    return render(request,"itinerary.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
