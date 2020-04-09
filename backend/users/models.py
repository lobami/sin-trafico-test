from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=80, null=True, unique=True, blank=True)
    email = models.EmailField(('email address'), unique=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=12, null=True)
    verification_key = models.UUIDField(default=uuid.uuid4, unique=True, null=False, editable=False)
    ROLES = (
        ('client', 'Cliente'),
        ('administrator', 'Administrador'),
    )
    role = models.CharField(max_length=50, null=False, choices=ROLES, default='Client')

