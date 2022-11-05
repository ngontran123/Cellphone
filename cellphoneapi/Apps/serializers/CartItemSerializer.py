from rest_framework import serializers

from ..services import ProductService, CartService
from ..shemas.CartSchema import Cart
from ..shemas.ProductSchema import Product
from ..shemas.CartItemSchema import CartItem
from ..shemas.CartSchema import Cart
from ..serializers.ProductSerializer import ProductSerializer
from ..serializers.CartSerializer import CartSerializer
from rest_framework.exceptions import ValidationError


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['pd'] = ProductSerializer(instance.pd).data
        response['cart'] = CartSerializer(instance.cart).data
        return response
