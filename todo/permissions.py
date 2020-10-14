from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Только владелец может править задачи"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
