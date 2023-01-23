from rest_framework import serializers

from network.models.retail_network import Retail_network


class Retail_networkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail_network
        fields = ('title',
                  'contacts',
                  'products',
                  'debt',
                  'created',
                  'updated'
                  )


class Retail_networkEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail_network
        fields = ('title',
                  'contacts',
                  'products',
                  'debt',
                  'created',
                  'updated'
                  )
        extra_kwargs = {
            'debt': {"read_only": True}
        }
