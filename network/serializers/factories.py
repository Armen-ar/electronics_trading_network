from rest_framework import serializers

from network.models.factory import Factory


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ('title',
                  'contacts',
                  'products',
                  'debt',
                  'created',
                  'updated'
                  )


class FactoryEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
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
