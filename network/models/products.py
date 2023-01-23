from django.db import models


class Products(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )

    model = models.CharField(
        verbose_name='Модель',
        max_length=255
    )

    created = models.DateTimeField(
        verbose_name='Дата выхода продукта на рынок'
    )
