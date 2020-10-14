from django_filters import rest_framework as filters

from .models import Todo


class TodoFilter(filters.FilterSet):
    """Поиск по заданным полям"""
    time_is_null = filters.BooleanFilter(field_name='planned_finish_time',
                                         lookup_expr='isnull')

    class Meta:
        model = Todo
        fields = ['status', 'planned_finish_time']
