from apps.api.serializers import EventSerializer
from asgiref.sync import sync_to_async
from apps.api.models import Event
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)


class EventService:
    def __init__(self):
        self.event = Event
        logger.info('INICIANDO EVENT SERVICE')

    @sync_to_async
    def save_event(self, data):
        event = self.event.objects.create(**data)
        logger.info(
            f'SAVE EVENT: (Lat: {event.lat}, Lng: {event.lng}, Category: {event.service_category_id})')
        return EventSerializer(event).data

    @ sync_to_async
    def load_events(self):
        events = list(self.event.objects.all())
        logger.info('GET ALL EVENTS')
        return [EventSerializer(event).data for event in events]
