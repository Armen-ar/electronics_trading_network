from rest_framework import generics

from network.models.private_trader import Private_trader
from network.serializers.private_trader import Private_traderSerializer, Private_traderEditSerializer


class Private_traderListCreateView(generics.ListCreateAPIView):
    queryset = Private_trader.objects.all()
    serializer_class = Private_traderSerializer

    def get_queryset(self):
        queryset = Private_trader.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contacts__country=country)
        return queryset


class Private_traderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Private_trader.objects.all()
    serializer_class = Private_traderEditSerializer
