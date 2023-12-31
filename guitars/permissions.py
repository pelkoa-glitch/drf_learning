from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    # Ограничение прав доступа на уровне всего запроса.
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    # Права доступа на уровне отдельного объекта(записи бд).
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
