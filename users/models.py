from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Введите адрес электронной почты"
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=20,
        verbose_name="Город",
        help_text="Укажите город",
        null=True,
        blank=True,
    )
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
