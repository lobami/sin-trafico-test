from django.utils import timezone
from django.db import models
import uuid


class Tracking(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    unit = models.ForeignKey('units.Unit', null=False, on_delete=models.CASCADE, related_name='tracking_unit')
    lat = models.DecimalField(max_digits=20, decimal_places=16)
    long = models.DecimalField(max_digits=20, decimal_places=16)
    date = models.DateTimeField(default=timezone.now)
