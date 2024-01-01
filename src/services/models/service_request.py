from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from services.models import Service

class ServiceRequest(models.Model):
    inquiry = models.TextField(_("inquiry"), blank=True)
    reply = models.TextField(_("reply"), default="", blank=True)
    desired_time = models.TimeField(_("desired time"), null=True, blank=True)
    desired_date = models.DateField(_("desired date"), null=False, blank=True)
    status = models.CharField(max_length=8, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ])
    client = models.ForeignKey(settings.AUTH_USER_MODEL, 
        verbose_name=_("client"), 
        on_delete=models.CASCADE, 
        related_name="service_requests", 
        null=False,
        blank=True
    )
    service = models.ForeignKey(Service, 
        verbose_name=_("service"), 
        on_delete=models.CASCADE, 
        related_name="service_requests", 
        null=False,
        blank=True
    )
    

    class Meta:
        verbose_name = _("service request")
        verbose_name_plural = _("service requests")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("service_request_detail", kwargs={"pk": self.pk})
