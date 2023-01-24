from django.urls import path

from network.views.factories import FactoryListCreateView, FactoryView
from network.views.private_trader import Private_traderListCreateView, Private_traderView
from network.views.retail_network import Retail_networkListCreateView, Retail_networkView

urlpatterns = [
    path('factory/list_create', FactoryListCreateView.as_view(), name='factory_list_create'),
    path('factory/<pk>', FactoryView.as_view(), name='factory_pk'),
    path('private_trader/list_create', Private_traderListCreateView.as_view(), name='private_trader_list_create'),
    path('private_trader/<pk>', Private_traderView.as_view(), name='private_trader_pk'),
    path('retail_network/list_create', Retail_networkListCreateView.as_view(), name='retail_network_list_create'),
    path('retail_network/<pk>', Retail_networkView.as_view(), name='retail_network_pk'),
]
