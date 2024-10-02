from django.contrib import admin
from .models import Client, Event, ClientEvent, Item, Purchase


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'total_exp',
                    'created_at',
                    'updated_at']
    search_fields = ['name', 'email']


class EventAdmin(admin.ModelAdmin):
    list_display = ['category',
                    'urgency',
                    'exp_acquired',
                    'reports_number',
                    'created_at',
                    'updated_at']

    search_fields = ['category']


class ClientEventAdmin(admin.ModelAdmin):
    list_display = ['client_id',
                    'event_id',
                    'created_at',
                    'updated_at']
    search_fields = ['client_id__name', 'event_id__category']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'type',
                    'value',
                    'created_at',
                    'updated_at']
    search_fields = ['title', 'type']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['client_id',
                    'item_id',
                    'created_at',
                    'updated_at']
    search_fields = ['client_id__name', 'item_id__title']


admin.site.register(Item, ItemAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(ClientEvent, ClientEventAdmin)
