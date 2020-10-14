from rest_framework import routers

from todo.views import TodoViewSet
from users.views import UserViewSet


router = routers.DefaultRouter()
router.register('todo', TodoViewSet, basename='todo')
router.register('users', UserViewSet, basename='users')
