from rest_framework import serializers

from users.models import User, Payments


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = (
            # "password",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
        )

    def get_payments(self, instance):
        return [payment.payment_date for payment in instance.users.filter(user=instance)]
