from django.conf import settings

MEDIAXML_ROOT = getattr(settings, 'MEDIAXML_ROOT', getattr(settings, 'MEDIA_ROOT', ''))