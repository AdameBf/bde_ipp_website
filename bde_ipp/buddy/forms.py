from django.forms import ModelForm

from .models import Buddlunteer


class BuddlunteersForm(ModelForm):
    class Meta:
        model = Buddlunteer
        fields = '__all__'


class BuddyForm(ModelForm):
    class Meta:
        model = Buddlunteer
        fields = '__all__'
