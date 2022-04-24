from django.forms import ModelForm

from .models import Buddlunteer, Buddy


class BuddlunteersForm(ModelForm):
    class Meta:
        model = Buddlunteer
        fields = '__all__'


class BuddyForm(ModelForm):
    class Meta:
        model = Buddy
        fields = '__all__'
