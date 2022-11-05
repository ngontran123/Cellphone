from rest_framework import serializers
from ..shemas.OrderStatusSchema import OrderStatusSchema


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusSchema
        fields = '__all__'

