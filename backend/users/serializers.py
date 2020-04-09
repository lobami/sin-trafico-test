from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from six import text_type


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

        return data


class UserSerializer(serializers.ModelSerializer):
    """
    General purpose user serializer.
    """

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'username', 'is_active', 'role',
            'phone'
        )


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Custom create user serializer that encrypt password.
    """

    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name', 'role',
            'password', 'phone'
        )

    def create(self, validated_data):
        """
        Get password field and encrypt it.
        """
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.username = validated_data['email']
        user.save()
        # send_activation(user)
        return user