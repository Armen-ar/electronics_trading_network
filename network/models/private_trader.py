from network.models.basic import Basic
from django.db import models

from network.models.retail_network import Retail_network


class Private_trader(Basic):
    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

    supplier = models.ForeignKey(
        Retail_network,
        verbose_name='Поставщик',
        on_delete=models.PROTECT
    )