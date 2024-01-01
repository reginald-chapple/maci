from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from providers.models import Schedule
from users.models import Client

# class BookingManager(models.Manager):
#     def filter_by_provider(self, provider):
#         return self.get_queryset().filter(service__provider=provider)


class Booking(models.Model):
    client = models.ForeignKey(Client, verbose_name=_("client"), on_delete=models.CASCADE, related_name="bookings", null=True, blank=True)
    schedules = models.ManyToManyField(Schedule, verbose_name=_("schedule"), related_name="bookings", blank=True)
    service = models.JSONField(_("service"), default=dict, blank=True)
    start_time = models.TimeField(_("start time"), null=False, blank=True)
    end_time = models.TimeField(_("end time"), null=True, blank=True)
    date = models.DateField(_("date"), null=False, blank=True)
    is_open = models.BooleanField(_("open status"), blank=True)
    duration = models.DurationField(_("duration"), null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ])
    # payment_information = models.TextField(default="", blank=True)  # Store payment details securely
    
    class Meta:
        verbose_name = _("booking")
        verbose_name_plural = _("bookings")
        
    # objects = BookingManager()

    def __str__(self):
        return self.client.identity.username

    def get_absolute_url(self):
        return reverse("booking_detail", kwargs={"pk": self.pk})
    
    
