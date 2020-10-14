from rest_framework.serializers import ModelSerializer, ReadOnlyField

from .models import Todo


class TodoSerializer(ModelSerializer):
    """Вывод списка заданий поля"""
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = '__all__'
