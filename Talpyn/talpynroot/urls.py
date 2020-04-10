from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('',                views.index,            name='index'),
    path('temp/',           views.temp,             name='temp'),
    path('authorization/',   views.authorization,    name = 'authorization'),
    path('registration/',    views.registration,     name = 'registration'),
    path("lesson/", views.lesson, name="lesson")
]