from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label = 'E-Mail')
    destination = forms.ChoiceField(choices=[('Los Angeles', 'Los Angeles'), ('Denver', 'Denver')])