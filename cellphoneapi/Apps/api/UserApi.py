import datetime

import jwt
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed
from ..serializers.UserSerializer import UserSerializer, LoginSerializer
from ..services import UserService
from django.contrib.auth.hashers import make_password


class Register(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        email = user['email']
        password = user['password']
        is_user, user_find = UserService.find_user_by_email(email)
        if not is_user:
            return Response(user_find)
        if not user_find.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        payload = {
            'username': user_find.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        payload_refresh = {
            'phone': user_find.phone,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=80),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        refresh_token = jwt.encode(payload_refresh, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.set_cookie(key='refresh_jwt', value=refresh_token, httponly=True)
        response.data = {
            'jwt': token,
            'refresh-jwt': refresh_token
        }
        return response


class UserDetail(generics.GenericAPIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Invalid account')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('The token is expired')

        is_user, user = UserService.find_user_by_name(payload['username'])
        if not is_user:
            return Response(user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailByResfresh(generics.GenericAPIView):
    def get(self, request):
        token = request.COOKIES.get('refresh_jwt')
        if not token:
            raise AuthenticationFailed('Invalid account')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('The token is expired')

        is_user, user = UserService.find_user_by_phone(payload['phone'])
        if not is_user:
            return Response(user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Logout(generics.GenericAPIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'delete token successfully'
        }
        return response


class UserViewList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        is_user, users = UserService.get_all_user()
        if not is_user:
            return Response(users)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserHandle(generics.GenericAPIView):
    serializer_class = UserSerializer

    def put(self, request, username, *args, **kwargs):
        is_user, user = UserService.find_user_by_name(username)
        if not is_user:
            return Response(user)
        user_object = request.data
        serializer = UserSerializer(user, data=user_object)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, username, *args, **kwargs):
        is_user, user = UserService.find_user_by_name(username)
        if not is_user:
            return Response(user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
