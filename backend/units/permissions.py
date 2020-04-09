from rest_framework.permissions import IsAuthenticated


class UnitPermission(IsAuthenticated):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
         return True

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.method in ['DELETE', 'PUT', 'GET', 'POST'] or request.user.role == 'administrator' \
                    or request.user == obj.user:
                return True

            return False


