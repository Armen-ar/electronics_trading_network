from django.db import models


class Contact(models.Model):
    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    email = models.EmailField(
        verbose_name="Логин.",
        unique=True,
        help_text="Не более 150 символов, только буквы, цифры и @/./+/-/_ @/./+/-/_.", )

    country = models.CharField(
        verbose_name='Страна',
        max_length=255
    )

    city = models.CharField(
        verbose_name='Город',
        max_length=255
    )

    street = models.CharField(
        verbose_name='Улица',
        max_length=255
    )

    house_number = models.CharField(
        verbose_name='Номер дома',
        max_length=255
    )
