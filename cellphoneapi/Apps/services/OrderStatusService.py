from ..shemas.OrderStatusSchema import OrderStatusSchema
from ..constants.error_code import ErrorCode, MSG_TEMPLATE
from typing import Tuple, List, Union


def get_all_order_status() -> Tuple[bool, Union[str, OrderStatusSchema]]:
    try:
        order_status = OrderStatusSchema.objects.all()
        return True, order_status
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]


def get_order_status_by_name(name) -> Tuple[bool, Union[str, OrderStatusSchema]]:
    order_status = OrderStatusSchema.objects.filter(status_name__icontains=name).first()
    if not order_status:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, order_status

