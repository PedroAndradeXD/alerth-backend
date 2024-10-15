import json
from apps.api.models import Event
from asgiref.sync import sync_to_async
from apps.api.serializers import EventSerializer
from channels.generic.websocket import AsyncWebsocketConsumer


class EventsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('events', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('events', self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        lat = text_data_json.get('lat')
        lng = text_data_json.get('lng')
        service_category_id = text_data_json.get(
            'service_category')

        # Save to database
        event = await sync_to_async(self.save_event)(lat, lng, service_category_id)

        await self.channel_layer.group_send(
            'events',
            {
                'type': 'new_event',
                'event': event
            }
        )

    async def new_event(self, event):
        await self.send(text_data=json.dumps(event))

    @sync_to_async
    def save_event(self, lat, lng, service_category_id):
        event = Event.objects.create(
            lat=lat, lng=lng, service_category_id=service_category_id)
        return EventSerializer(event).data
