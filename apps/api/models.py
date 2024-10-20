from uuid import uuid4
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import re

from .utils import load_blacklist


class Client(models.Model):
    client_id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=128)
    total_exp = models.PositiveIntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class Item(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid4)
    type = models.CharField(max_length=70)
    value = models.PositiveIntegerField()
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Purchase(models.Model):
    purchase_id = models.UUIDField(primary_key=True, default=uuid4)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client.name} - {self.item.title}'


class ServiceEntity(models.Model):
    service_entity_id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    service_category_id = models.UUIDField(primary_key=True, default=uuid4)
    category = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid4)
    service_category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE
    )
    lat = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    lng = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    reports_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_category.category} - {self.reports_number} reports"


class ClientEvent(models.Model):
    client_event_id = models.UUIDField(primary_key=True, default=uuid4)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client.name} - {self.event.category}'


class EntityCategory(models.Model):
    entity_category_id = models.UUIDField(primary_key=True, default=uuid4)
    service_entity = models.ForeignKey(
        ServiceEntity, on_delete=models.CASCADE)
    service_category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    exp_acquired = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.service_entity.name} - {self.service_entity.category}'


class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid4)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    BLACKLIST = load_blacklist()

    def clean_comment(self, comment):
        for word in self.BLACKLIST:
            comment = re.sub(rf'\b{word}\b', '*' *
                             len(word), comment, flags=re.IGNORECASE)
        return comment

    def save(self, *args, **kwargs):
        self.comment = self.clean_comment(self.comment)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comment
