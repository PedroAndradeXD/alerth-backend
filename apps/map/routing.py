from django.urls import re_path
from .consumers import MapConsumer

websocket_urlpatterns = [
    re_path(r'ws/', MapConsumer.as_asgi()),
]
