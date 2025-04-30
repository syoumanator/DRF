from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, PaymentsListApiView, UserRetrieveAPIView, UserCreateAPIView, \
    UserDestroyAPIView, PaymentsCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name = UsersConfig.name

urlpatterns = [
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user-detail"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user-update"),
    path("payments/", PaymentsListApiView.as_view(), name="payments-list"),

    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("<int:pk>/delete/", UserDestroyAPIView.as_view(), name="delete"),
    path("payments/create/", PaymentsCreateAPIView.as_view(), name="create-payments"),
]
