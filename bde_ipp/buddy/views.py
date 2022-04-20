from django.shortcuts import render

# Create your views here.
from .forms import BuddyForm, BuddlunteersForm
from .models import Buddlunteer


def buddlunteers_form(request):
    # TODO: Add a form to the page
    if request.method == 'POST':
        instance = Buddlunteer()
        form = BuddlunteersForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = BuddlunteersForm()

    return render(request, 'buddy/buddy_form.html', {'form': form})


def buddy_form(request):
    # TODO: Add a form to the page
    if request.method == 'POST':
        form = BuddyForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'buddy/buddy_form.html')


def choice_page(request):
    return render(request, 'buddy/choice_page.html')
