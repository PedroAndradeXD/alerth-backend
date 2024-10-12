from django.urls import path, include
from rest_framework.routers import DefaultRouter
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

# Adicionando as URLs do router
urlpatterns = [
    path('', include(router.urls)),
]
