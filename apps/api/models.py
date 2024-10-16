from uuid import uuid4
from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Client(models.Model):
    client_id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=128)
    total_exp = models.PositiveIntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  # Facilita a leitura do objeto no admin

    def set_password(self, raw_password):
        # Transforma a senha em um hash
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        # Compara a senha do usuário com o hash
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
        return f'{self.serviceEntity_id.name} - {self.serviceCategory_id.category}'


class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid4)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
