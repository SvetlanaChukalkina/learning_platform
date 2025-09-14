from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(
        max_length=15, verbose_name="Номер телефона", blank=True, null=True
    )
    city = models.CharField(max_length=35, verbose_name="Город", blank=True, null=True)
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    """Модель платежа"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    date = models.DateField(verbose_name="Дата платежа")
    payment_for_course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Плата за курс")
    payment_for_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Плата за урок")
    total_payment = models.PositiveIntegerField(verbose_name="Сумма платежа")
    type = models.CharField (max_length=15, help_text="Способ оплаты: наличные или перевод", verbose_name="Способ оплаты")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"