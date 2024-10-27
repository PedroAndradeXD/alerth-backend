from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .services import EventService
import json


class MapConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, event_service=None):
        super().__init__()
        self.event_service = event_service or EventService()

    async def connect(self):
        print(f"Conectando: {self.channel_name}")
        await self._join_event_group()
        await self.accept()
        await self._send_initial_events()

    async def receive(self, text_data):
        print(f"Recebido: {text_data}")
        await self._handle_event_received(text_data)

    async def new_event(self, event):
        print(f"Novo evento recebido: {event['event']}")
        await self._send_event(event['event'])

    async def disconnect(self, close_code):
        print(f"Desconectado: {self.channel_name} com código: {close_code}")
        await self._leave_event_group()

    async def _join_event_group(self):
        await self.channel_layer.group_add('events', self.channel_name)
        print(f"Adicionado ao grupo de eventos: {self.channel_name}")

    async def _leave_event_group(self):
        await self.channel_layer.group_discard('events', self.channel_name)
        print(f"Removido do grupo de eventos: {self.channel_name}")

    async def _send_initial_events(self):
        events_data = await self.event_service.load_events()
        await self.send(self._serialize_data(events_data))

    async def _handle_event_received(self, text_data):
        data = self._deserialize_data(text_data)
        saved_event = await self.event_service.save_event(data)
        await self._broadcast_new_event(saved_event)

    async def _broadcast_new_event(self, event):
        print(f"Transmitindo novo evento: {event}")
        await self.channel_layer.group_send('events', {
            'type': 'new_event',
            'event': event
        })

    async def _send_event(self, event):
        await self.send(self._serialize_data({'event': event}))

    def _serialize_data(self, data):
        serialized_data = json.dumps(data)
        return serialized_data

    def _deserialize_data(self, text_data):
        data = json.loads(text_data)
        return data
