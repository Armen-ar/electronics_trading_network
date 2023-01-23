from rest_framework import generics

from network.models.retail_network import Retail_network
from network.serializers.retail_network import Retail_networkSerializer, Retail_networkEditSerializer


class Retail_networkListView(generics.ListAPIView):
    queryset = Retail_network.objects.all()
    serializer_class = Retail_networkSerializer

    def get_queryset(self):
        queryset = Retail_network.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contacts__country=country)
        return queryset


class Retail_networkCreateView(generics.CreateAPIView):
    queryset = Retail_network.objects.all()
    serializer_class = Retail_networkSerializer


class Retail_networkView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Retail_network.objects.all()
    serializer_class = Retail_networkEditSerializer
