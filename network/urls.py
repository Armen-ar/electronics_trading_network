from django.urls import path

from network.views.factories import FactoryListView, FactoryCreateView, FactoryView
from network.views.private_trader import Private_traderListView, Private_traderCreateView, Private_traderView
from network.views.retail_network import Retail_networkListView, Retail_networkCreateView, Retail_networkView

urlpatterns = [
    path('factory/list', FactoryListView.as_view(), name='factory_list'),
    path('factory/create', FactoryCreateView.as_view(), name='factory_create'),
    path('factory/<pk>', FactoryView.as_view(), name='factory_pk'),
    path('private_trader/list', Private_traderListView.as_view(), name='private_trader_list'),
    path('private_trader/create', Private_traderCreateView.as_view(), name='private_trader_create'),
    path('private_trader/<pk>', Private_traderView.as_view(), name='private_trader_pk'),
    path('retail_network/list', Retail_networkListView.as_view(), name='retail_network_list'),
    path('retail_network/create', Retail_networkCreateView.as_view(), name='retail_network_create'),
    path('retail_network/<pk>', Retail_networkView.as_view(), name='retail_network_pk'),
]
