from django.shortcuts import render

def rop_en(request):
    return render(request, 'documents/rop_en.html')

def rop_fr(request):
    return render(request, 'documents/rop_fr.html')
    
def statutes_en(request):
    return render(request, 'documents/statutes_en.html')

def statutes_fr(request):
    return render(request, 'documents/statutes_fr.html')
