from rest_framework.response import Response
from rest_framework import generics, status
from ..services import UserService, RoleService
from ..serializers.RoleSerializer import RoleSerializer
from rest_framework.exceptions import AuthenticationFailed


class RoleListView(generics.ListAPIView):
    serializer_class = RoleSerializer

    def get(self, request, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        is_role, roles = RoleService.get_all_role()
        if not is_role:
            return Response(roles)
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        role_object = request.data
        role_name = role_object['role_name']
        is_role, role = RoleService.get_role_by_name(role_name)
        if is_role:
            return Response('This role has been added to the database.')
        serializer = RoleSerializer(data=role_object)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoleApiView(generics.GenericAPIView):
    serializer_class = RoleSerializer

    def get(self, request, id, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        is_role, role = RoleService.get_role_by_id(id)
        if not is_role:
            return Response(role)
        serializer = RoleSerializer(role)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        is_role, role = RoleService.get_role_by_id(id)
        role_object = request.data
        if not is_role:
            return Response(role)
        serializer = RoleSerializer(role, data=role_object)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        is_role, role = RoleService.get_role_by_id(id)
        if not is_role:
            return Response(role)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoleNameApiView(generics.GenericAPIView):
    serializer_class = RoleSerializer

    def get(self, request, name, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        is_role, role = RoleService.get_role_by_name(name)
        if not is_role:
            return Response(role)
        serializer = RoleSerializer(role)
        return Response(serializer.data, status=status.HTTP_200_OK)
