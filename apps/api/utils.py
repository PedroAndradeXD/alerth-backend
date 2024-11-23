import json
from django.conf import settings


def load_blacklist():
    with open(settings.BASE_DIR / 'blacklist.json') as f:
        data = json.load(f)
    return data['blacklist']
    
