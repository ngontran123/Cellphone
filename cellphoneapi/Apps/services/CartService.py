import datetime

from rest_framework.response import Response

from ..shemas.CartSchema import Cart
from ..constants.error_code import ErrorCode, MSG_TEMPLATE
from typing import Tuple, List, Union
from ..serializers import CartSerializer
from ..services import UserService
from rest_framework.exceptions import ValidationError


def get_all_cart() -> Tuple[bool, Union[str, Cart]]:
    try:
        carts = Cart.objects.all()
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, carts


def get_cart_by_id(id) -> Tuple[bool, Union[str, Cart]]:
    try:
        cart = Cart.objects.get(id=id)
        if not cart:
            return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, cart


def mapping_cart(cart_obj, username):
    cart_object = {
        'username': username,
        'created_date': datetime.datetime.now(),
        'updated_date': datetime.datetime.now(),
        'total_price': 0,
        'total_weight': 0
    }
    return cart_object


def get_cart_by_username(username) -> Tuple[bool, Union[str, Cart]]:
    try:
        cart = Cart.objects.filter(username__icontains=username).first()
        if not cart:
            return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, cart
