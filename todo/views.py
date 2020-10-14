from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from .models import Todo
from .permissions import IsOwner
from .serializers import TodoSerializer
from .service import TodoFilter


class TodoViewSet(ModelViewSet):
    """Вывод списка заданий"""
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsOwner,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TodoFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset
