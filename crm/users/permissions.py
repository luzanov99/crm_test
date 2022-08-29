from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_superuser)


class IsAdminOrUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.user.is_authenticated and obj.pk == request.user.pk\
                and request.method != 'DELETE':
            return True
