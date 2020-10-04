"""Serializers User"""
from django.contrib.auth import authenticate, password_validation
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from htch.users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )


class UserSignUpSerializers(serializers.Serializer):
    """Serializador de registro de usuario"""
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        passwd = data['password']
        password_conf = data['password_confirmation']
        if passwd != password_conf:
            raise serializers.ValidationError('Password no coinciden')
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user


class UserLoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Credenciales invalidas')
        self.context['user'] = user
        return data

    def create(self, data):
        """Genera un nuevo token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
