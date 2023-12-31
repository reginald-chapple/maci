from datetime import datetime
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Provider(models.Model):
    alias = models.CharField(_('alias'), max_length=255, blank=True)
    identity = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("identity"), primary_key=True, on_delete=models.CASCADE, related_name="provider")
    qualifications = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    # skills = models.ManyToManyField('Skill', blank=True)
    location = models.CharField(max_length=255, blank=True)
    ratings = models.FloatField(default=0.0)  # Implement a rating system

    class Meta:
        verbose_name = _("provider")
        verbose_name_plural = _("providers")

    def __str__(self):
        return self.alias

    def get_absolute_url(self):
        return reverse("provider_detail", kwargs={"pk": self.pk})
