from django.shortcuts import render

# Create your views here.
from .forms import BuddyForm, BuddlunteersForm
from .models import Buddlunteer, Buddy


def buddlunteers_form_view(request):
    if request.method == 'POST':
        instance = Buddlunteer()
        form = BuddlunteersForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = BuddlunteersForm()

    return render(request, 'buddy/buddlunteer_form.html', {'form': form})


def buddy_form_view(request):
    if request.method == 'POST':
        instance = Buddy()
        form = BuddyForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = BuddyForm()

    return render(request, 'buddy/buddy_form.html', {"form": form})


def choice_page(request):
    return render(request, 'buddy/choice_page.html')
