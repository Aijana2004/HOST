import django_filters
from .models import *


class PropertyFilter(django_filters.FilterSet):

    class Meta:
        model = Property
        fields = {
            'price': ['lt', 'gt'],
            'city': ['exact', ],
            'property_type': ['exact', ],
            'rules': ['exact', ],
        }