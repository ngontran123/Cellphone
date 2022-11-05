from ..shemas.CartItemSchema import CartItem
from ..constants.error_code import ErrorCode, MSG_TEMPLATE
from ..shemas.CartSchema import Cart
from typing import Tuple, List, Union
from ..services import CartService, ProductService
from ..serializers import CartItemSerializer
from rest_framework.exceptions import ValidationError


def get_all_cart_items() -> Tuple[bool, Union[str, CartItem]]:
    try:
        cart_items = CartItem.objects.all()
    except:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, cart_items


def get_cart_items_by_id(id) -> Tuple[bool, Union[str, CartItem]]:
    try:
        cart_item = CartItem.objects.filter(id=id).first()
        if not cart_item:
            return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, cart_item


def get_cart_items_by_cart_id(cart_id) -> Tuple[bool, Union[str, CartItem]]:
    try:
        cart_item = CartItem.objects.filter(cart__id=cart_id)
        if not cart_item:
            return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, cart_item


def check_product_exists_in_cart(cart_id, product_id) -> Tuple[bool, Union[str, CartItem]]:
    is_cart, cart = CartService.get_cart_by_id(cart_id)
    if not is_cart:
        return False, 'Cannot find cart'
    is_cart_items, cart_items = get_cart_items_by_cart_id(cart_id)
    if not is_cart_items:
        return False, 'Cannot find cart_items for this cart'
    for item in cart_items:
        if item.pd.id == product_id:
            return True, item
    return False, ErrorCode.NOT_FOUND


def add_cart_items(object,cart_id):
    product_id = object['pd']
    is_product, product = ProductService.get_product_by_id(product_id)
    is_cart, cart= CartService.get_cart_by_id(cart_id)
    if not is_product:
        raise ValidationError("Cannot find this product id")
    if not is_cart:
        raise ValidationError("Cannot find this cart id")
    new_cart_items = {
        'price': product.price,
        'weight': product.weight,
        'quantity': object['quantity'],
        'product_name': product.name,
        'pd': product_id,
        'cart': cart_id
    }
    return new_cart_items
