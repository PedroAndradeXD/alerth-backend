from rest_framework import viewsets
from .models import (Client, Event, ClientEvent,
                     Item, Purchase, EntityCategory)
from .serializers import (ClientSerializer, EventSerializer,
                          ClientEventSerializer, ItemSerializer, PurchaseSerializer, EntityCategorySerializer)

from .models import ServiceEntity, ServiceCategory, EntityCategory
from .serializers import ServiceEntitySerializer, ServiceCategorySerializer, EntityCategorySerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ClientEventViewSet(viewsets.ModelViewSet):
    queryset = ClientEvent.objects.all()
    serializer_class = ClientEventSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class ServiceEntityViewSet(viewsets.ModelViewSet):
    queryset = ServiceEntity.objects.all()
    serializer_class = ServiceEntitySerializer


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer


class EntityCategoryViewSet(viewsets.ModelViewSet):
    queryset = EntityCategory.objects.all()
    serializer_class = EntityCategorySerializer
