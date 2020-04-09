from rest_framework import viewsets
from units.models import Unit
from center.pagination import ResultSetPagination
from .serializers import UnitSerializer, UnitCreateSerializer
from .permissions import UnitPermission


class UnitViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a unit instance.
    list:
        Return all unit's, ordered by name.
    create:
        Create a new unit.
    delete:
        Remove an existing unit.
    partial_update:
        Update one or more fields on an existing unit.
    update:
        Update one or more fields on an existing unit.
    """

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    pagination_class = ResultSetPagination
    permission_classes = (UnitPermission,)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST']:
            return UnitCreateSerializer
        return UnitSerializer

    def get_queryset(self, *args, **kwargs):
        """
        Get all query params and create an object to filter data, excluding empty fields.
        """
        if self.request.query_params:
            data = {}

            for param in self.request.query_params:
                _param = self.request.query_params.get(param, '')
                if param not in ['items', 'page', 'id', 'user', 'plates'] and _param != '':
                    data[param + '__icontains'] = _param

            return Unit.objects.filter(**data)

        return Unit.objects.all()

