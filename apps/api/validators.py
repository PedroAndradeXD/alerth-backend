from rest_framework import serializers
from .models import Client, Event, ClientEvent, Item, Purchase, ServiceEntity, ServiceCategory, EntityCategory
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


def validate_name(value):
    if len(value) < 3:
        raise serializers.ValidationError("O nome deve conter pelo menos 3 caracteres.")
    return value

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'name', 'email', 'total_exp', 'created_at', 'updated_at']
        read_only_fields = ['client_id', 'created_at', 'updated_at']

    
    def validate_email(self, value):
        EmailValidator()(value)
        
        if Client.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso.")
        return value


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_id', 'lat', 'lng', 'category', 'urgency', 'exp_acquired', 'reports_number', 'created_at', 'updated_at']
        read_only_fields = ['event_id', 'created_at', 'updated_at']

    def validate_lat(self, value):
        if not (-90 <= value <= 90):
            raise serializers.ValidationError("A latitude deve estar entre -90 e 90 graus.")
        return value

    def validate_lng(self, value):
        if not (-180 <= value <= 180):
            raise serializers.ValidationError("A longitude deve estar entre -180 e 180 graus.")
        return value

    def validate_urgency(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("A urgência deve estar entre a escala de 1 a 5.")
        return value


class ClientEventSerializer(serializers.ModelSerializer):
    client_id = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:
        model = ClientEvent
        fields = ['client_id', 'event_id', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        client = data.get('client_id')
        event = data.get('event_id')

        if not client or not event:
            raise serializers.ValidationError("Cliente ou evento inválido.")
        
        if ClientEvent.objects.filter(client_id=client, event_id=event).exists():
            raise serializers.ValidationError("Este cliente já está associado a este evento.")
        
        return data


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_id', 'type', 'value', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['item_id', 'created_at', 'updated_at']

    def validate_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor do item deve ser positivo.")
        return value


class PurchaseSerializer(serializers.ModelSerializer):
    client_id = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())

    class Meta:
        model = Purchase
        fields = ['purchase_id', 'client_id', 'item_id', 'created_at', 'updated_at']
        read_only_fields = ['purchase_id', 'created_at', 'updated_at']

    def validate(self, data):
        client = data.get('client_id')
        item = data.get('item_id')

        if client.total_exp < item.value:
            raise serializers.ValidationError(" Experiência insuficiente.")
        
        return data

class ServiceEntitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = ServiceEntity
        fields = ['serviceEntity_id', 'name', 'created_at']
        read_only_fields = ['serviceEntity_id', 'created_at']


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['serviceCategory_id', 'category', 'created_at']
        read_only_fields = ['serviceCategory_id', 'created_at']


    def validate_category(self, value):
        if ServiceCategory.objects.filter(category=value).exists():
            raise serializers.ValidationError("Essa categoria já existe.")
        return value


class EntityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityCategory
        fields = ['entityCategory_id', 'serviceEntity_id', 'serviceCategory_id', 'created_at']
        read_only_fields = ['entityCategory_id', 'created_at']

def validate(self, data):
        if EntityCategory.objects.filter(serviceEntity_id=data['serviceEntity_id'], serviceCategory_id=data['serviceCategory_id']).exists():
            raise serializers.ValidationError("Essa combinação de entidade e categoria já existe.")
        return data