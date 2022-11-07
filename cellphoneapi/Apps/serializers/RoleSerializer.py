from rest_framework import serializers
from ..shemas.RoleSchema import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

