from datetime import timedelta
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.choices import DAY_OF_WEEK_CHOICES

class Schedule(models.Model):
    day = models.PositiveSmallIntegerField(_("day of week"), choices=DAY_OF_WEEK_CHOICES, null=False, blank=True)
    opening_time = models.TimeField(_("opening time"), null=False, blank=True)
    closing_time = models.TimeField(_("closing time"), null=False, blank=True)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, 
        verbose_name=_("provider"), 
        on_delete=models.CASCADE, 
        related_name="schedules", 
        null=False,
        blank=True,
    )

    class Meta:
        verbose_name = _("schedule")
        verbose_name_plural = _("schedules")

    def __str__(self):
        return f"{self.provider.alias} - {self.day}"

    def get_absolute_url(self):
        return reverse("schedule_detail", kwargs={"pk": self.pk})
    
    def get_booked_hours(self):
        """
        Returns a list of tuples representing the booked hours for a given schedule and date.
        Each tuple contains the start and end time of a booked hour.
        """
        """ 0 - Monday
            1 - Tuesday
            2 - Wednesday
            3 - Thursday
            4 - Friday
            5 - Saturday
            6 - Sunday
        """
        bookings = self.bookings.filter(date__week_day=self.day)
        booked_hours = []
        for booking in bookings:
            start_time = booking.start_time
            end_time = booking.end_time
            booked_hours.append((start_time, end_time))
        return booked_hours
    
    
    def get_available_hours(self):
        """
        Returns a list of tuples representing the available hours for a given schedule and date.
        Each tuple contains the start and end time of an available hour.
        """
        booked_hours = set()
        
        bookings = self.bookings.all()
        
        for booking in bookings:
            booked_hours.update(range(booking.start_time.hour, booking.end_time.hour + 1))
            
        all_hours = set(range(self.opening_time.hour, self.closing_time.hour + 1))
        available_hours = all_hours - booked_hours

        return list(available_hours)