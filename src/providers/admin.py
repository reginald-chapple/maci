from django.contrib import admin

from providers.models import Provider, Schedule, Skill

admin.site.register(Provider)
admin.site.register(Schedule)
admin.site.register(Skill)
