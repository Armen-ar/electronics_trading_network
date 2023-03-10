from rest_framework import generics
from network.models.factory import Factory
from network.serializers.factories import FactorySerializer, FactoryEditSerializer


class FactoryListCreateView(generics.ListCreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

    def get_queryset(self):
        queryset = Factory.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contacts__country=country)
        return queryset


class FactoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryEditSerializer
