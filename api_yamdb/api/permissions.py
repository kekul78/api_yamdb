from rest_framework import permissions


class IsAuthorModeratorAadminOrReadOnly(permissions.BasePermission):
    """Класс для проверки доступа - админ, модератор - только чтение."""
    def has_permission(self, request, view):
        """Проверка наличия доступа."""
        return (
            (request.method in permissions.SAFE_METHODS)
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """Проверка наличия доступа."""
        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
            or request.user.is_moderator
            or request.user.is_admin
        )


class IsAdmin(permissions.BasePermission):
    """Класс для проверки доступа - админ."""
    def has_permission(self, request, view):
        """Проверка наличия доступа."""
        return request.user.is_authenticated and (
            request.user.is_admin)


class IsAdminOrReadOnly(IsAdmin):
    """Класс для проверки доступа - админ - только чтение."""
    def has_permission(self, request, view):
        """Проверка наличия доступа."""
        return (
            request.method in permissions.SAFE_METHODS
            or super().has_permission(request, view)
        )
