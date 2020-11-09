from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from query_db import QueryHandler
# Create your views here.

def home_view(request, *args, **kwargs):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.isvalid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         print(name, email)
    form = ContactForm()
    return render(request, "home.html", {'form': form})


def recommendation_view(request):
    if request.method == 'POST':
        # get the form data that was submitted from home page
        form = ContactForm(request.POST)
        if form.is_valid():
            # extract form data that was entered
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            dest = form.cleaned_data['destination']

    query_handler = QueryHandler()
    row = query_handler.queryRecommendations(dest, "destination")
    #construct context containing database and form information to pass into html page
    
    query_handler.close_conn()
    return render(request, "recommendations.html", {'destination': dest, 'country': row[2], 'summary': row[3], 'user': name})
