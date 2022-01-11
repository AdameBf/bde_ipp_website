from django import forms
import datetime

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=32, required=True, label='First Name',widget=forms.TextInput(attrs={'class': 'form-text'}))
    last_name = forms.CharField(max_length=32, required=True, label='Last Name',widget=forms.TextInput(attrs={'class': 'form-text'}))
    email = forms.EmailField(required=True, label='E-mail address',widget=forms.EmailInput(attrs={'class': 'form-text'}))
    address = forms.CharField(max_length=255, required=True, label='Address (Number, Street, Postal Code, Town)',widget=forms.TextInput(attrs={'class': 'form-text'}))
    birth_date = forms.DateField(required=True, label='Date of Birth', initial=datetime.date.today,widget=forms.DateInput(attrs={'class': 'form-text'}))
    programme_type = forms.ChoiceField(required=True, label='Programme',
        choices=[('m1', 'Master 1'), ('m2', 'Master 2'), ('phd', 'PhD track')],widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))
    programme_name = forms.CharField(max_length=63, label='',widget=forms.TextInput(attrs={'class': 'form-text'}))  # Specify exact programme followed
    statutes_rop_agreement = forms.BooleanField(required=True, label=
    """
    I accept and acknowledge the Statutes and the Rules of Procedure of the association.
    I promise to pay my membership fee in accordance with the conditions described in the Rules of Procedure.
    """,widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
