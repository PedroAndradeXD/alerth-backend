from apps.api.serializers import EventSerializer
from asgiref.sync import sync_to_async
from apps.api.models import Event, ServiceCategory
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)


class EventService:
    def __init__(self):
        self.event = Event
        self.service_category = ServiceCategory
        logger.info('INICIANDO EVENT SERVICE')

    @sync_to_async
    def save_event(self, data):
        service_category = self.service_category.objects.get(
            service_category_id=data.get("service_category"))

        event = Event.objects.create(
            lat=data.get("lat"),
            lng=data.get("lng"),
            service_category=service_category
        )

        logger.info(
            f'SAVE EVENT: (Lat: {event.lat}, Lng: {event.lng}, Category: {event.service_category_id})')
        return EventSerializer(event).data

    @ sync_to_async
    def load_events(self):
        events = list(self.event.objects.all())
        logger.info('GET ALL EVENTS')
        return [EventSerializer(event).data for event in events]
