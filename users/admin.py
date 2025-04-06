from django.contrib import admin
from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ("password",)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    fields = ("user", "paid_course", "paid_lesson", "payment_amount", "payment_method")