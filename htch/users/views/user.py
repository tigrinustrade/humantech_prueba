from django.contrib.auth import get_user_model
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from htch.users import serializers as serializer_users
from htch.users.permissions import IsAccountOwner

User = get_user_model()


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
        mixins.ListModelMixin):
    """ViewSet que controla el sign up y login
    """
    queryset = User.objects.all()
    serializer_class = serializer_users.UserModelSerializer

    
    def get_permissions(self):
        """Asigna permisos basado en accines"""
        if self.action in ['signup', 'login']:
            permissions = [AllowAny]
        if self.action in ['list', 'retrieve']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAdminUser]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """Registro de usuario"""
        serializer = serializer_users.UserSignUpSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer_users.UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        """Logea un usuario"""
        serializer = serializer_users.UserLoginSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': serializer_users.UserModelSerializer(user).data,
            'acces_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
