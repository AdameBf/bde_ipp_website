from django.shortcuts import render
from .forms import RegistrationForm


# Handle account registration
def register(request):
    if request.method == 'POST':
        # Perform checks
        pass
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register/register.html', context)
