from django.forms import ModelForm

from .models import Buddlunteer, Buddy


class BuddlunteersForm(ModelForm):
    class Meta:
        model = Buddlunteer
        exclude = ['has_matched']


class BuddyForm(ModelForm):
    class Meta:
        model = Buddy
        exclude = ['associated_buddlunteer']
