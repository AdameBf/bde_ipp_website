from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=512, required=True)
    birth_date = forms.DateField(required=True)

