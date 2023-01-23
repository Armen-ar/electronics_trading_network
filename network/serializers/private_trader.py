from rest_framework import serializers

from network.models.private_trader import Private_trader


class Private_traderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Private_trader
        fields = ('title',
                  'contacts',
                  'products',
                  'debt',
                  'created',
                  'updated'
                  )


class Private_traderEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Private_trader
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
