from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label = 'E-Mail')
    destination = forms.ChoiceField(choices=[('Los Angeles', 'Los Angeles'), ('Denver', 'Denver')])

class FlightForm(forms.Form):
    home_aiport = forms.CharField()
    dest_airport = forms.CharField()
    departure_date = forms.DateField()
    return_date = forms.DateField()