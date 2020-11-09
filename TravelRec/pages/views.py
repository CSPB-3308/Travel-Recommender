from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
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


def choose_city(request):
    if request.method == 'POST':
        # get the form data that was submitted from home page
        form = ContactForm(request.POST)
        if form.is_valid():
            # extract form data that was entered
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            dest = form.cleaned_data['destination']

    return HttpResponse(dest)
