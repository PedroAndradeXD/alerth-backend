import json
from channels.generic.websocket import AsyncWebsocketConsumer


class EventsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('events', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('events', self.channel_name)

    async def receive(self, text_data):
        # Recebe a mensagem e a converte para JSON
        text_data_json = json.loads(text_data)
        lat = text_data_json.get('lat', None)
        lng = text_data_json.get('lng', None)

        # Envia a mensagem para o grupo "events"
        await self.channel_layer.group_send(
            'events',
            {
                'type': 'coords',
                'lat': lat,
                'lng': lng
            }
        )

    async def coords(self, event):
        lat = event.get('lat', None)
        lng = event.get('lng', None)

        # Envia as coordenadas de volta para o WebSocket
        await self.send(text_data=json.dumps({
            'lat': lat,
            'lng': lng
        }))
