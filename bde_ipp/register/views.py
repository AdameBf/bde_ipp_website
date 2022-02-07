from django.shortcuts import render
from .forms import RegistrationForm
from .models import Member


# Handle account registration
def register(request):
    if request.method == 'POST':
        # Perform checks
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the registration
            new_member = Member()
            new_member.first_name = form.cleaned_data['first_name']
            new_member.last_name = form.cleaned_data['last_name']
            new_member.birth_date = form.cleaned_data['birth_date'] # TODO: ensure no absurd date has been provided!
            new_member.email = form.cleaned_data['email']
            new_member.address = form.cleaned_data['address']
            new_member.master_level = form.cleaned_data['master_level']
            new_member.phd_track = form.cleaned_data['phd_track']
            new_member.programme_name = form.cleaned_data['programme_name']
            new_member.save()
            return render(request, 'register/success.html')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register/register.html', context)
