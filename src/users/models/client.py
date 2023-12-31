from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Client(models.Model):
    identity = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("identity"), primary_key=True, on_delete=models.CASCADE, related_name="client")
    

    class Meta:
        verbose_name = _("client")
        verbose_name_plural = _("clients")

    def __str__(self):
        return self.identity.username

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"pk": self.pk})
