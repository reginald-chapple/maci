from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from providers.models import Provider
from services.models import Category

class Service(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="services", null=False, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    images = models.ImageField(upload_to='services/', blank=True)
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.CASCADE, related_name="services", null=False, blank=True)
    cancellation_policy = models.TextField(default="", blank=True)
    duration = models.DurationField(_("duration"), null=True, blank=True)

    class Meta:
        verbose_name = _("service")
        verbose_name_plural = _("services")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"pk": self.pk})
