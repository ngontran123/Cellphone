from rest_framework import serializers

from ..shemas.CartItemSchema import CartItem
from ..serializers.ProductSerializer import ProductSerializer
from ..serializers.CartSerializer import CartSerializer


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['pd'] = ProductSerializer(instance.pd).data
        response['cart'] = CartSerializer(instance.cart).data
        return response
