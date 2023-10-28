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
                    request.user.role == 'admin' or request.user.is_superuser
                )))


class IsAuthorModeratorAadminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        return (request.user.is_authenticated and (
            request.user == obj.author
            or request.user.role == 'moderator'
            or request.user.role == 'admin'
        ))


class IsAdmin(permissions.BasePermission):
    """
    Класс для проверки доступа - админ.
    """
    def has_permission(self, request, view):
        """
        Проверка наличия доступа.
        """
        return request.user.is_authenticated and (
            request.user.user.role == 'admin' or request.user.is_superuser)
