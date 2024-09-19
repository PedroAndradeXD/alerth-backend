from django.urls import path
from django.http import HttpResponse
from . import views


def returnResponde(request):
    return HttpResponse('Olá')


# Definindo as URLs
urlpatterns = [
    path('endpoint/', returnResponde, name='apps'),
]
