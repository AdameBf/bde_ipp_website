from django.shortcuts import render
from .forms import RegistrationForm

# Handle account registration
def register(request):
    if request.method == 'POST':
        # Perform checks
        pass
    else:
        form = RegistrationForm(request.POST)
    context = {
        'forms': form
    }
    return render(request, 'portal/register.html', context)