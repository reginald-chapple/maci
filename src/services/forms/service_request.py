from django import forms

from services.models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    inquiry = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    desired_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    desired_time = forms.TimeField(
        required=True,
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    )
    class Meta:
        model = ServiceRequest
        fields = ("inquiry","desired_time","desired_date")
