from django.contrib.auth.models import AbstractUser
from django.db import models
from education.models import Course, Lesson



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


class Payments(models.Model):
    CASH = "Наличные"
    TRANSFER_TO_AN_ACCOUNT = "Перевод на счет"

    METHOD_CHOICES = ((CASH, "Наличные"), (TRANSFER_TO_AN_ACCOUNT, "Перевод на счет"))

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users",
        verbose_name="Пользователь",
    )
    payment_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата оплаты",
        null=True,
        blank=True,
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="Оплаченный курс",
        null=True,
        blank=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Оплаченный урок",
        null=True,
        blank=True,
    )
    payment_amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(
        max_length=50, verbose_name="Способ оплаты", choices=METHOD_CHOICES
    )

    def __str__(self):
        return f"{self.user} - {self.paid_course if self.paid_course else self.paid_lesson}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
