from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=32, required=True, label='First Name')
    last_name = forms.CharField(max_length=32, required=True, label='Last Name')
    email = forms.EmailField(required=True, label='E-mail address')
    address = forms.CharField(max_length=256, required=True, label='Address (Number, Street, Postal Code, Town)')
    birth_date = forms.DateField(required=True, label='Date of Birth')
    statutes_rop_agreement = forms.BooleanField(required=True, label=
    """
    I accept and acknowledge the Statutes and the Rules of Procedure of the association.
    I promise to pay the membership fees in accordance with the conditions described in the Rules of Procedure.
    """)

