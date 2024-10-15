from rest_framework import serializers
from .models import Client, Event, Item


class EmailValidator:
    def __call__(self, value):
        if '@' not in value:
            raise serializers.ValidationError("Invalid email address.")


class PositiveValueValidator:
    def __call__(self, value):
        if value <= 0:
            raise serializers.ValidationError("Value must be positive.")


class ClientNameValidator:
    def __call__(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Name must be at least 3 characters long.")
