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


