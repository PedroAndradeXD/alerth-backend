from rest_framework import serializers
from .models import Event, Client, ClientEvent, Item, Purchase

# Serializer para o modelo Client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client # Associa o serializer ao modelo
        fields = ['client id', 'name', 'email', 'password', 'total exp', 'created at', 'updated at'] #campos que serão incluídos na serialização

# Serializer para o modelo Event
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event id', 'lat', 'lng', 'category', 'urgency', 'exp acquired', 'reports number', 'created at', 'updated at', 'tittle', 'description', 'location', 'date', 'user']

# Serializer para o modelo ClientEvent
class ClientEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientEvent
        fields = ['client id', 'event id', 'created at', 'updated at']

# Serializer para o modelo Item
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item id', 'type', 'value', 'title', 'description', 'created at', 'updated at']

# Serializer para o modelo Purchase
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['purchase id', 'client id', 'item id' 'created at', 'updated at']
