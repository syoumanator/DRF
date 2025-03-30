from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
