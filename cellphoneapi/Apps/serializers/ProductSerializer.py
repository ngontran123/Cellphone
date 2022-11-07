from rest_framework import serializers
from ..shemas.ProductSchema import Product
from ..serializers.ProductDetailSerializer import ProductDetailSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['pd_detail'] = ProductDetailSerializer(instance.pd_detail).data
        return response
