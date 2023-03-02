from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet

from authorization.api.v1.views import AuthorizationMixin

from .serializers import UserSerializer


class UserViewSet(AuthorizationMixin, ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
