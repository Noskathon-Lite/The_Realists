from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TransportationForm
from .models import EmissionsSummary

def calculator_view(request):
    transportation = None
    if request.method == 'POST':
        form = TransportationForm(request.POST)
        if form.is_valid():
            transportation = form.save()
            messages.success(request, f'Successfully calculated emissions!')
    else:
        form = TransportationForm()
    
    context = {
        'form': form,
        'transportation': transportation,  # Pass the latest calculation
    }
    return render(request, 'calculator.html', context)

def emissions_history(request):
    # Get all transportation records
    records = Transportationmodel.objects.all().order_by('-id')
    summary = EmissionsSummary.objects.first()
    
    context = {
        'records': records,
        'summary': summary
    }
    return render(request, 'history.html', context)
