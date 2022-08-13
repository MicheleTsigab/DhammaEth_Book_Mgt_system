import django_filters

from .models import Instance

class InstanceFilter(django_filters.FilterSet):
    class Meta:
        model = Instance
        fields = ['book__title', 'id']