from django.shortcuts import render

# Create your views here.

def Register(request):
    return render(request, 'Register.html')

def logIN(request):
    return render(request, 'logIN.html')

