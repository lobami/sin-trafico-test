from .models import User
from .serializers import UserSerializer, CreateUserSerializer
from rest_framework import viewsets, status
from center.pagination import ResultSetPagination
from .permissions import UserPermission
from rest_framework.decorators import action
from rest_framework.response import Response
from units.models import Unit
from units.serializers import UnitSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.
    list:
        Return all users, ordered by name.
    create:
        Create a new user.
    delete:
        Remove an existing user.
    partial_update:
        Update one or more fields on an existing user.
    update:
        Update one or more fields on an existing user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = ResultSetPagination
    permission_classes = (UserPermission,)

    def get_serializer_class(self):
        """
        Use different serializer in create action to manage password.
        """
        return CreateUserSerializer if self.action == 'create' else UserSerializer

    def get_queryset(self, *args, **kwargs):

        """
        Get all query params and create an object to filter data, excluding empty fields.
        """

        if self.request.query_params:
            data = {}

            for param in self.request.query_params:
                _param = self.request.query_params.get(param, '')
                if param not in ['items', 'page', ] and _param != '':
                    data[param + '__icontains'] = _param

            return User.objects.filter(**data)

        return User.objects.all()

    @action(methods=['GET'], detail=True)
    def units(self, request, pk):
        """
        Return the unit's of the user.
        """
        user = self.get_object()
        units = Unit.objects.filter(user=user)
        units = UnitSerializer(units, many=True).data
        return Response(units, status=status.HTTP_200_OK)