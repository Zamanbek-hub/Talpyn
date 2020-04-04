from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.index, name='index'),
    path('temp/', views.temp, name='temp'),
]