from django.db import models


class Course(models.Model):
    """Модель курса"""

    name = models.CharField(max_length=150, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="materials/course/photo", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(verbose_name="Описание курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель урока"""

    name = models.CharField(max_length=150, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока")
    preview = models.ImageField(
        upload_to="materials/course/photo", blank=True, null=True, verbose_name="Превью"
    )
    link = models.URLField(verbose_name="Ссылка на урок")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
