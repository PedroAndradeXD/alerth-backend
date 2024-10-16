from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .services import EventService
import json


class MapConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, event_service=None):
        super().__init__()
        self.event_service = event_service or EventService()

    async def connect(self):
        await self.channel_layer.group_add('events', self.channel_name)
        await self.accept()
        events_data = await self.event_service.load_events()
        await self.send(json.dumps(events_data))

    async def receive(self, text_data):
        data = json.loads(text_data)
        saved_event = await self.event_service.save_event(data)
        await self.channel_layer.group_send('events', {
            'type': 'new_event',
            'event': saved_event
        })

    async def new_event(self, event):
        await self.send(json.dumps({
            'event': event['event']
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('events', self.channel_name)
        print('Desconectado')
