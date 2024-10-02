from rest_framework import serializers
from .models import Client, Event, ClientEvent, Item, Purchase


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id',
                  'name',
                  'email',
                  'total_exp',
                  'created_at',
                  'updated_at']
        read_only_fields = ['client_id', 'created_at', 'updated_at']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_id',
                  'lat',
                  'lng',
                  'category',
                  'urgency',
                  'exp_acquired',
                  'reports_number',
                  'created_at',
                  'updated_at']
        read_only_fields = ['event_id', 'created_at', 'updated_at']


class ClientEventSerializer(serializers.ModelSerializer):
    client_id = ClientSerializer(read_only=True)
    event_id = EventSerializer(read_only=True)

    class Meta:
        model = ClientEvent
        fields = ['client_id',
                  'event_id',
                  'created_at',
                  'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_id',
                  'type',
                  'value',
                  'title',
                  'description',
                  'created_at',
                  'updated_at']
        read_only_fields = ['item_id', 'created_at', 'updated_at']


class PurchaseSerializer(serializers.ModelSerializer):
    client_id = ClientSerializer(read_only=True)
    item_id = ItemSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = ['purchase_id',
                  'client_id',
                  'item_id',
                  'created_at',
                  'updated_at']

        read_only_fields = ['purchase_id', 'created_at', 'updated_at']
