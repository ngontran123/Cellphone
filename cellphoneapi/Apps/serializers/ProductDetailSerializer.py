from rest_framework import serializers
from ..shemas.ProductDetailSchema import ProductDetail


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'
