from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
        )