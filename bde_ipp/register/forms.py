from django import forms
import datetime

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=32, required=True, label='First Name')
    last_name = forms.CharField(max_length=32, required=True, label='Last Name')
    email = forms.EmailField(required=True, label='E-mail address')
    address = forms.CharField(max_length=255, required=True, label='Address (Number, Street, Postal Code, Town)')
    birth_date = forms.DateField(required=True, label='Date of Birth', initial=datetime.date.today)
    programme_type = forms.ChoiceField(required=True, label='Programme',
        choices=[('m1', 'Master 1'), ('m2', 'Master 2'), ('phd', 'PhD track')])
    programme_name = forms.CharField(max_length=127, label='')  # Specify exact programme followed
    statutes_rop_agreement = forms.BooleanField(required=True, label=
    """
    I accept and acknowledge the Statutes and the Rules of Procedure of the association.
    I promise to pay my membership fee in accordance with the conditions described in the Rules of Procedure.
    """)
