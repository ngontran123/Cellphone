from rest_framework import serializers
from ..models import User
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'phone')
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
        regex = re.compile(r"^[\d\-\+]{9,15}$")
        if phone and not re.fullmatch(regex, phone):
            raise serializers.ValidationError("Invalid phone number")
        else:
            return data


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
        regex = re.compile(r"^[\d\-\+]{9,15}$")
        if phone and not re.fullmatch(regex, phone):
            raise serializers.ValidationError("Invalid phone number")
        else:
            return data


