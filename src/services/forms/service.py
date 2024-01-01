from django import forms

from classifications.models import Category
from services.models import Service

class ServiceForm(forms.ModelForm):
    name = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    price_per_hour = forms.DecimalField(max_value=500000, min_value=1, max_digits=6, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    category = cause = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Service
        fields = ("name","description","price_per_hour","category")
