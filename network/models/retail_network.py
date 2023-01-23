from network.models.basic import Basic
from django.db import models

from network.models.factory import Factory


class Retail_network(Basic):
    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    supplier = models.ForeignKey(
        Factory,
        verbose_name='Поставщик',
        on_delete=models.PROTECT
    )
