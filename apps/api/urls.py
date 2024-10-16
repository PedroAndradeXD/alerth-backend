from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
# from . import views
from .viewsets import ClientViewSet, EventViewSet, ClientEventViewSet, ItemViewSet, PurchaseViewSet, EntityCategoryViewSet, ServiceEntityViewSet, ServiceCategoryViewSet

# Criando o router e registrando os viewsets
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'events', EventViewSet)
router.register(r'client-events', ClientEventViewSet)
router.register(r'items', ItemViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'service-category', ServiceCategoryViewSet)
router.register(r'entity-category', EntityCategoryViewSet)
router.register(r'service-entity', ServiceEntityViewSet)

# Definindo as URLs
urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', views.login),
    # path('signup', views.signup),
    # path('test_token.', views.test_token),

    path('', include(router.urls)),
]
