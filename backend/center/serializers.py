from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.six import text_type
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super(TokenObtainPairSerializer, self).validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = text_type(refresh)
        data['token'] = text_type(refresh.access_token)
        data['rol_id'] = self.user.role
        data['user_id'] = self.user.id
        data['username'] = self.user.username

        return data
