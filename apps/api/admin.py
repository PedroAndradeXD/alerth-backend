from django.contrib import admin
from .models import (Client, Event, ClientEvent, Item, Purchase,
                     Comment, ServiceCategory, ServiceEntity, EntityCategory)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'total_exp',
                    'created_at',
                    'updated_at']
    search_fields = ['name', 'email']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['service_category',
                    'reports_number',
                    'created_at',
                    'updated_at']

    search_fields = ['category']


@admin.register(ClientEvent)
class ClientEventAdmin(admin.ModelAdmin):
    list_display = ['client_id',
                    'event_id',
                    'created_at',
                    'updated_at']
    search_fields = ['client_id__name', 'event_id__category']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'type',
                    'value',
                    'created_at',
                    'updated_at']
    search_fields = ['title', 'type']


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['purchase_id', 'client_id',
                    'item_id',
                    'created_at',
                    'updated_at']
    search_fields = ['client_id__name', 'item_id__title']
    readonly_fields = ['purchase_id']


@admin.register(EntityCategory)
class EntityCategoryAdmin(admin.ModelAdmin):
    list_display = ('entity_category_id', 'service_entity_id',
                    'service_category_id', 'created_at')
    search_fields = ('service_entity_id__name',
                     'service_category_id__category')
    list_filter = ('created_at',)
    ordering = ('created_at',)
    readonly_fields = ('entity_category_id', 'created_at')


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('service_category_id', 'category', 'created_at')
    search_fields = ('category',)
    list_filter = ('created_at',)
    ordering = ('created_at',)
    readonly_fields = ('service_category_id', 'created_at')


@admin.register(ServiceEntity)
class ServiceEntityAdmin(admin.ModelAdmin):
    list_display = ('service_entity_id', 'name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('created_at',)
    readonly_fields = ('service_entity_id', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'client',
                    'event', 'comment', 'created_at')
    search_fields = ('client__name', 'event__name', 'comment')
    list_filter = ('created_at',)
    ordering = ('created_at',)
    readonly_fields = ('comment_id', 'created_at')

# admin.site.register(Item, ItemAdmin)
# admin.site.register(Event, EventAdmin)
# admin.site.register(Client, ClientAdmin)
# admin.site.register(Purchase, PurchaseAdmin)
# admin.site.register(Comments, CommentsAdmin)
# admin.site.register(ClientEvent, ClientEventAdmin)
