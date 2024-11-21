from rest_framework import serializers
from .models import Client, Event, ClientEvent, Item, Purchase, ServiceCategory, ServiceEntity, EntityCategory, Comment
from .validators import EmailValidator, PositiveValueValidator, ClientNameValidator
from django.contrib.auth.models import User
from django.db.models import Q


class ClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    name = serializers.CharField(validators=[ClientNameValidator()])

    class Meta:
        model = Client
        fields = ['client_id', 'name', 'email',
                  'total_exp', 'created_at', 'updated_at']
        read_only_fields = ['client_id', 'created_at', 'updated_at']

class ClientLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, data):
        email = data['email']
        password = data['password']
        
        # Verifica se o usuário existe com email ou username
        try:
            user = User.objects.get(Q(email__iexact=email) | Q(username__iexact=email))
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuário não encontrado.")

        # Verifica a senha
        if not user.check_password(password):
            raise serializers.ValidationError("Senha incorreta!")

        # Retorna o objeto do usuário
        return user


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['service_category', 'description', 'lat', 'lng',
                  'reports_number', 'created_at', 'updated_at']
        read_only_fields = ['event_id', 'created_at', 'updated_at']


class ClientEventSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = ClientEvent
        fields = ['client_event_id',
                  'client',
                  'event',
                  'created_at',
                  'updated_at']
        read_only_fields = ['client', 'client_event_id',
                            'created_at', 'updated_at']


class ItemSerializer(serializers.ModelSerializer):
    value = serializers.FloatField(validators=[PositiveValueValidator()])

    class Meta:
        model = Item
        fields = ['item_id', 'type', 'value', 'title',
                  'description', 'created_at', 'updated_at']
        read_only_fields = ['item_id', 'created_at', 'updated_at']


class PurchaseSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = ['purchase_id', 'client',
                  'item', 'created_at', 'updated_at']
        read_only_fields = ['purchase_id', 'created_at', 'updated_at']


class ServiceEntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceEntity
        fields = ['service_entity_id',
                  'name',
                  'created_at']


class ServiceCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCategory
        fields = ['service_category_id',
                  'category',
                  'created_at']


class EntityCategorySerializer(serializers.ModelSerializer):
    service_entity = ServiceEntitySerializer(read_only=True)
    service_category = ServiceCategorySerializer(read_only=True)

    class Meta:
        model = EntityCategory
        fields = ['entity_category_id',
                  'service_entity',
                  'service_category',
                  'created_at',
                  'exp_acquired']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id', 'client', 'event', 'comment']
