import uuid
from django.db import models
from trackings.models import Tracking


class Unit(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey('users.User', null=True, on_delete=models.CASCADE, related_name='unit_user')
    plates = models.CharField(max_length=50, null=True, blank=True)

    @property
    def lat(self):
        if Tracking.objects.filter(unit=self.id).exists():
            return Tracking.objects.filter(unit=self.id).order_by('-date').first().lat
        else:
            return None

    def long(self):
        if Tracking.objects.filter(unit=self.id).exists():
            return Tracking.objects.filter(unit=self.id).order_by('-date').first().long
        else:
            return None
