from rest_framework import viewsets
from .models import Client, Event, ClientEvent, Item, Purchase
from .serializers import ClientSerializer, EventSerializer, ClientEventSerializer, ItemSerializer, PurchaseSerializer


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

