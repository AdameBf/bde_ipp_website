from django.shortcuts import render

# Handle account registration
def register(request):
    if request.method == 'POST':
        # Perform checks
        pass
    else:
        form = UserCreationForm(request.POST)
    context = {
        'forms': form
    }
    return render(request, 'portal/register.html', context)