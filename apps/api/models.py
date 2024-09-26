from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=128)
    total_exp = models.IntegerField()

    def _str_(self):
        return self.name #pra facilitar a leitura do objeto no admin
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password) #transforma a senha em um hash

    def check_password(self, raw_password):
        return check_password(raw_password, self.password) #compara a senha do usuario com o hash

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    category = models.CharField(max_length=70)
    reports_number = models.IntegerField()
    urgency = models.IntegerField()
    exp_aquired = models.IntegerField()

    def _str_(self):
        return self.category
    
class ClientEvent(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.client.name} - {self.event.category}'
    
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=70)
    valor = models.IntegerField()
    title = models.CharField(max_length=70)
    description = models.TextField()

    def _str_(self):
        return self.title

class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
         return f'{self.client.name} - {self.item.title}'
