import django_filters

from ..models import Task


class TaskFilter(django_filters.FilterSet):
    creator = django_filters.CharFilter(field_name='creator', lookup_expr='exact')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['creator', 'description', 'name']
