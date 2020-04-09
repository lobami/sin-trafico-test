from rest_framework import serializers
from .models import Unit
from users.serializers import UserSerializer


class UnitSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Unit
        fields = ('id', 'name', 'user', 'plates', 'lat', 'long')


class UnitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name', 'user', 'plates')
