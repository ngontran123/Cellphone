import datetime

from ..shemas.OrderItemSchema import OrderItemSchema
from ..constants.error_code import ErrorCode, MSG_TEMPLATE
from typing import Tuple, List, Union


def get_order_items() -> Tuple[bool, Union[str, List[OrderItemSchema]]]:
    try:
        orders = OrderItemSchema.objects.all()
        return True, orders
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]


def get_order_item_by_id(id) -> Tuple[bool, Union[str, OrderItemSchema]]:
    order_item = OrderItemSchema.objects.filter(id=id).first()
    if not order_item:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, order_item


d
