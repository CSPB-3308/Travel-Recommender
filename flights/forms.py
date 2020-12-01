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

class DateInput(forms.DateInput):
    input_type = 'date'

class FlightForm(forms.Form):
    home_airport = forms.CharField()
    destination_airport = forms.CharField()
    departure_date = forms.DateField(widget=DateInput)
    return_date = forms.DateField(widget=DateInput)
