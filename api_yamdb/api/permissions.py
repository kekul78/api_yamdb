from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Класс для проверки доступа - админ - только чтение.
    """
    def has_permission(self, request, view):
        """
        Проверка наличия доступа.
        """
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and (
                    request.user.is_admin or request.user.is_superuser)))


class IsAdminModeratorOwnerOrReadOnly(permissions.BasePermission):
    """
    Класс для проверки доступа - админ, модератор - только чтение.
    """
    def has_object_permission(self, request, view, obj):
        """
        Проверка наличия доступа.
        """
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin
                or request.user.is_moderator
                or obj.author == request.user)

    def has_permission(self, request, view):
        """
        Проверка наличия доступа.
        """
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)


class IsAdmin(permissions.BasePermission):
    """
    Класс для проверки доступа - админ.
    """
    def has_permission(self, request, view):
        """
        Проверка наличия доступа.
        """
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)
