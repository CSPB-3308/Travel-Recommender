from django import forms
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'

cities = ["", "Abu Dhabi", "Adelaide", "Albuquerque", "Alicante", "Amsterdam", "Anaheim", "Anchorage",
        "Annapolis", "Asheville", "Athens", "Atlanta", "Auckland", "Austin", "Baltimore", "Bangkok", "Barcelona",
        "Baton Rouge", "Beijing", "Berlin", "Boca Raton", "Boston", "Brisbane", "Brussels", "Budapest", "Buenos Aires",
        "Burlington", "Cabo San Lucas", "Cairo", "Calgary", "Cannes", "Cape Town", "Charleston", "Charlotte", "Chicago",
        "Copenhagen", "Cozumel", "Dallas", "Denver", "Dubai", "Dublin", "Edinburgh", "Fairbanks", "Flagstaff",
        "Fort Lauderdale", "Fort Myers", "Galveston", "Galway", "Geneva", "Glasgow", "Greenville", "Hamburg", "Havana",
        "Hong Kong", "Honolulu", "Houston", "Ibiza", "Indianapolis", "Istanbul", "Johannesburg", "Kansas City", "Las Vegas",
        "Lima", "Lisbon", "London", "Los Angeles", "Madison", "Madrid", "Manchester", "Marrakech", "Melbourne", "Memphis",
        "Mexico City", "Miami", "Milan", "Milwaukee", "Moscow", "Myrtle Beach", "Naples", "Nashville", "New Orleans",
        "New York", "Nice", "Oklahoma City", "Omaha", "Orlando", "Oslo", "Ottawa", "Palm Springs", "Panama City Beach", "Paris",
        "Pensacola", "Perth", "Phoenix", "Phuket", "Pittsburgh", "Portland", "Prague", "Puerto Vallarta", "Quebec City",
        "Raleigh", "Reno", "Richmond", "Rio de Janeiro", "Rome", "Sacramento", "Salt Lake City", "Salzburg", "San Antonio",
        "San Diego", "San Francisco", "San Jose", "Santa Barbara", "Santa Fe", "Santo Domingo", "Savannah", "Seattle",
        "Seoul", "Shanghai", "Singapore", "Stockholm", "Sydney", "Tallahassee", "Tampa", "Tokyo", "Toronto", "Tucson",
        "Tulsa", "Vancouver"]


CITY_CHOICES= [tuple([x,x]) for x in cities]

class ContactForm(forms.Form):
    home = forms.CharField(label='Home:', widget=forms.Select(choices=CITY_CHOICES), required=True)
    destination = forms.CharField(label='Home:', widget=forms.Select(choices=CITY_CHOICES), required=True)
    outdate = forms.CharField( required=True)
    indate = forms.CharField(required=True)