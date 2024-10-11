from django.urls import path
from django.http import HttpResponse
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def returnResponde(request):
    return HttpResponse('Olá')


# Definindo as URLs
urlpatterns = [
    path('endpoint/', returnResponde, name='apps'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', views.login),
    path('signup', views.signup),
    path('test_token', views.test_token),
]
