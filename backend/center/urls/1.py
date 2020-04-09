from rest_framework import routers
from django.urls import include
from django.conf.urls import url
from users.views import UserViewSet
from units.views import UnitViewSet
from trackings.views import TrackingViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'units', UnitViewSet)
router.register(r'trackings', TrackingViewSet)
urlpatterns = [
    url(r'', include(router.urls)),
]