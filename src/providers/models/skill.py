from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Skill(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("skill_detail", kwargs={"pk": self.pk})
