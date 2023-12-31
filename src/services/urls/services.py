from django.urls import include, path

from services import views

urlpatterns = [
    path('services/', include(([
        path('', views.all, name='all'),
        path('<int:id>/', views.details, name='details'),
        path('<int:id>/book/', views.book, name='book'),
    ], 'services'))),
]