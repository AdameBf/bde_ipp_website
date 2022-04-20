import datetime

from django import forms
from django.forms import ModelForm
from .models import Buddlunteer


class BuddlunteersForm(ModelForm):
    class Meta:
        model = Buddlunteer
        fields = '__all__'


class BuddyForm(forms.Form):
    pass
