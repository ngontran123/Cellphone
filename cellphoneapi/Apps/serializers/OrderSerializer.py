from rest_framework import serializers
from ..shemas.OrderSchema import OrderSchema
from ..shemas.OrderStatusSchema import OrderStatusSchema
from ..serializers.OrderStatusSerializer import OrderStatusSerializer
from rest_framework.exceptions import ValidationError
from ..services import UserService


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSchema
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['status'] = OrderStatusSerializer(instance.status).data
        return response

    def validate(self, data):
        username = data.get('username')
        is_user, user = UserService.find_user_by_name(username)
        if not is_user:
            raise ValidationError("Invalid user")
        return data
