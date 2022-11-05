from rest_framework import serializers

from ..services import ProductService, CartService
from ..shemas.OrderItemSchema import OrderItemSchema
from ..shemas.OrderSchema import OrderSchema
from rest_framework.exceptions import ValidationError
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
