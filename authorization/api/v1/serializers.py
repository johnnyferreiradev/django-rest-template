from rest_framework import serializers
from django.contrib.auth import password_validation


class PasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        allow_blank=False, allow_null=False)
    new_password = serializers.CharField(allow_blank=False, allow_null=False)

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value
