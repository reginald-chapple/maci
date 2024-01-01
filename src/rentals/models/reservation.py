from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from rentals.models import Rental

class Reservation(models.Model):
    renter = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("renter"), on_delete=models.CASCADE, related_name="reservations", null=True, blank=True)
    rental = models.ForeignKey(Rental, verbose_name=_("rental"), on_delete=models.SET_NULL, related_name="reservations", null=True, blank=True)
    procurement_time = models.TimeField(_("procurement time"), null=False, blank=True)
    return_time = models.TimeField(_("return time"), null=True, blank=True)
    rental_date = models.DateField(_("rental date"), null=False, blank=True)
    return_date = models.DateField(_("return date"), null=False, blank=True)
    deposit = models.DecimalField(verbose_name=_("deposit"), max_digits=10, decimal_places=2, blank=True)
    total = models.DecimalField(verbose_name=_("total"), max_digits=10, decimal_places=2, blank=True)
    procurement_method = models.CharField(verbose_name=_("procurement method"), max_length=20, choices=[
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
    ])
    status = models.CharField(verbose_name=_("status"), max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('declined', 'Declined'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("reservation")
        verbose_name_plural = _("reservations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("reservation_detail", kwargs={"pk": self.pk})
