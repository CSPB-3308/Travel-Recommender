from django import forms

from .models import testFlightData

class CreateFlightForm(forms.ModelForm):
    class Meta:
        model = testFlightData
        fields = ['flightNum',
                  'origin',
                  'destination',
                  'flightDateTime',
                  'flightCost'
                  ]

class FlightForm(forms.Form):
    home_aiport = forms.CharField()
    dest_airport = forms.CharField()
    departure_date = forms.DateField()
    return_date = forms.DateField()
