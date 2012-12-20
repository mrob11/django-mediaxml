from django.views.generic import TemplateView

from mediaxml.settings import MEDIAXML_ROOT

class MediaXMLView(TemplateView):
    
    template_name = ''