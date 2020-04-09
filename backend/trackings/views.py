from rest_framework import viewsets
from .models import Tracking
from center.pagination import ResultSetPagination
from .serializers import TrackingSerializer


class TrackingViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a tracking instance.
    list:
        Return all tracking's, ordered by name.
    create:
        Create a new tracking.
    delete:
        Remove an existing tracking.
    partial_update:
        Update one or more fields on an existing tracking.
    update:
        Update one or more fields on an existing tracking.
    """

    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
    pagination_class = ResultSetPagination

    def get_queryset(self, *args, **kwargs):
        """
        Get all query params and create an object to filter data, excluding empty fields.
        """
        if self.request.query_params:
            data = {}

            for param in self.request.query_params:
                _param = self.request.query_params.get(param, '')
                if param not in ['items', 'page', 'id', 'user', 'unit'] and _param != '':
                    data[param + '__icontains'] = _param

            return Tracking.objects.filter(**data)

        return Tracking.objects.all()

