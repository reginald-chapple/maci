from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from classifications.models import Category

class Rental(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("owner"), on_delete=models.CASCADE, related_name="rentals",  blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    daily_rate = models.DecimalField(verbose_name=_("daily rate"), max_digits=10, decimal_places=2, blank=True)
    images = models.ImageField(upload_to='services/', blank=True)
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.CASCADE, related_name="services", null=False, blank=True)
    cancellation_policy = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("rental")
        verbose_name_plural = _("rentals")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rental_detail", kwargs={"pk": self.pk})
