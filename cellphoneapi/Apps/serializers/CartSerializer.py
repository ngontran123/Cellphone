from rest_framework import serializers
from ..shemas.CartSchema import Cart
from rest_framework.exceptions import ValidationError
from ..services import UserService


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def validate(self, data):
        username = data.get('username')
        is_user, user = UserService.find_user_by_name(username)
        if not is_user:
            raise ValidationError("Invalid user")
        return data
