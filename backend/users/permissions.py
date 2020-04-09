from rest_framework.permissions import IsAuthenticated


class UserPermission(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        if request.user and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True
        if request.user and request.user.is_authenticated:
            actions = ['GET', 'PUT', 'DELETE']
            if request.method in actions:
                return True
            return True


