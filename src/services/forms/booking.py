from django import forms

from services.models import Booking

class BookingForm(forms.ModelForm):
    TIME_INPUT_FORMATS = ['%H:%M', '%H%M']

    date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    start_time = forms.TimeField(
        required=True,
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    )
    class Meta:
        model = Booking
        fields = ("date","start_time")
