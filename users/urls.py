from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView,  PaymentsListApiView, UserRetrieveAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user-detail"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user-update"),
    path("payments/", PaymentsListApiView.as_view(), name="payments-list"),
]