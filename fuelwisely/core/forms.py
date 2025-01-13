from django import forms
from .models import Transportationmodel

class TransportationForm(forms.ModelForm):
    class Meta:
        model = Transportationmodel
        fields = ['vehicle_type', 'distance', 'mode', 'vehicle_size']
        widgets = {
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'mode': forms.Select(attrs={'class': 'form-control'}),
            'vehicle_size': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_distance(self):
        distance = self.cleaned_data['distance']
        if distance <= 0:
            raise forms.ValidationError("Distance must be greater than 0")
        return distance 