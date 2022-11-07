from rest_framework import serializers
from ..models import User
import re
from ..shemas.RoleSchema import Role
from ..serializers.RoleSerializer import RoleSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'phone', 'car_id', 'role_id')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        username = validated_data.get('username', None)
        email = validated_data.get('email', None)
        phone = validated_data.get('phone', None)
        car_id = validated_data.get('car_id', None)
        role_id = validated_data.get('role_id', None)
        if password is not None:
            instance.set_password(password)
            instance.username = username
            instance.email = email
            instance.phone = phone
            instance.car_id = car_id
            instance.role_id = role_id
        instance.save()
        return instance

    def validate(self, data):
        phone = data.get('phone')
        regex = re.compile(r"^[\d\-\+]{9,15}$")
        if phone and not re.fullmatch(regex, phone):
            raise serializers.ValidationError("Invalid phone number")
        else:
            return data

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['role_id'] = RoleSerializer(instance.role_id).data
        return response


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def validate(self, data):
        phone = data.get('phone')
        role_id = data.get('role_id')
        car_id = data.get('car_id')
        regex = re.compile(r"^[\d\-\+]{9,15}$")
        if phone and not re.fullmatch(regex, phone):
            raise serializers.ValidationError("Invalid phone number")
        if role_id == 3:
            if car_id == '':
                raise serializers.ValidationError('Car Id is required for shipper account')
        else:
            return data

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        username = validated_data.get('username', None)
        email = validated_data.get('email', None)
        phone = validated_data.get('phone', None)
        car_id = validated_data.get('car_id', None)
        role_id = validated_data.get('role_id', None)
        if password is not None:
            instance.set_password(password)
            instance.username = username
            instance.email = email
            instance.phone = phone
            instance.car_id = car_id
            instance.role_id = role_id
        instance.save()
        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['role_id'] = RoleSerializer(instance.role_id).data
        return response
