from rest_framework import serializers

from ..shemas.OrderItemSchema import OrderItemSchema

from ..serializers.ProductSerializer import ProductSerializer
from ..serializers.OrderSerializer import OrderSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemSchema
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['pd'] = ProductSerializer(instance.pd).data
        response['order'] = OrderSerializer(instance.order).data
        return response
