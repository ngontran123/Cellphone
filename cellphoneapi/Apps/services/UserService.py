import jwt

from ..models import User
from ..constants.error_code import ErrorCode, MSG_TEMPLATE
from typing import Tuple, List, Union
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

def find_user_by_email(email) -> Tuple[bool, Union[str, User]]:
    user = User.objects.filter(email=email).first()
    if not user:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, user


def find_user_by_name(name) -> Tuple[bool, Union[str, User]]:
    user = User.objects.filter(username=name).first()
    if not user:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, user


def find_user_by_phone(phone) -> Tuple[bool, Union[str, User]]:
    user = User.objects.filter(phone=phone).first()
    if not user:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, user


def get_username_by_token(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise ValidationError("Not log in yet.")
    try:
        user = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise ValidationError('The token has expired')
    is_user, user_find = find_user_by_name(user['username'])
    if not is_user:
        raise ValidationError('Cannot find this user')
    return user_find.username


def get_all_user() -> Tuple[bool, Union[str, List[User]]]:
    try:
        users = User.objects.all()
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, users


def get_role_by_token(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise ValidationError('Not log in yet')
    try:
        user = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise ValidationError('token has been expired')
    is_user, user_find = find_user_by_name(user['username'])
    if not is_user:
        raise ValidationError('Cannot find this user')
    role = user_find.role_id.id
    return role


