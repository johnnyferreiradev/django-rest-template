from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import PasswordSerializer


class AuthorizationMixin(object):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class PasswordViewSet(AuthorizationMixin, APIView):
    def post(self, request):
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = request.user
            if not user.check_password(
                serializer.validated_data.get("current_password")
            ):
                raise PermissionDenied()

            user.set_password(serializer.validated_data.get("new_password"))
            user.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
