from rest_framework import serializers
from .models import Client, Event, ClientEvent, Item, Purchase, ServiceCategory, ServiceEntity, EntityCategory, Comments


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


class ServiceEntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceEntity
        fields = ['servic_entity_id',
                  'name',
                  'created_at']


class ServiceCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCategory
        fields = ['serviceCategory_id',
                  'category',
                  'created_at']


class EntityCategorySerializer(serializers.ModelSerializer):
    serviceEntity = ServiceEntitySerializer(read_only=True)
    serviceCategory = ServiceCategorySerializer(read_only=True)

    class Meta:
        model = EntityCategory
        fields = ['entityCategory_id',
                  'serviceEntity',
                  'serviceCategory',
                  'created_at']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment_id', 
                  'client_id', 
                  'event_id', 
                  'comment']