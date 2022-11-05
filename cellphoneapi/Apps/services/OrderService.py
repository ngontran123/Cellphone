import datetime

from ..shemas.OrderSchema import OrderSchema
from ..constants.error_code import ErrorCode, MSG_TEMPLATE
from typing import Tuple, List, Union


def get_all_order() -> Tuple[bool, Union[str, List[OrderSchema]]]:
    try:
        orders = OrderSchema.objects.all()
        return True, orders
    except:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]


def get_order_by_id(id) -> Tuple[bool, Union[str, OrderSchema]]:
    order = OrderSchema.objects.filter(id=id).first()
    if not order:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, order


def get_order_by_username(username) -> Tuple[bool, Union[str, OrderSchema]]:
    order = OrderSchema.objects.filter(username=username).first()
    if not order:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, order
