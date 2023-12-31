from django.contrib import admin

from services.models import Service, Category, Booking

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Booking)
