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


def check_valid_date(date):
    try:
        year, month, day = date.split('-')
    except Exception as e:
        return False
    is_valid = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_valid = False
    return is_valid


def convert_datetime_to_date(datetime):
    datetime = str(datetime)
    date = datetime.date()
    return date


def get_order_between_two_dates(from_date, to_date) -> Tuple[bool, Union[str, List[OrderSchema]]]:
    from_date = int(from_date)
    to_date = int(to_date)
    if not check_valid_date(from_date):
        return False, 'From_date is not a valid date'
    if not check_valid_date(to_date):
        return False, 'To_date is not a valid date'
    y_first, m_first, d_first = from_date.split('-')
    y_second, m_second, d_second = to_date.split('-')
    date_first = datetime.date(int(y_first), int(m_first), int(d_first))
    date_second = datetime.date(int(y_second), int(m_second), int(d_second))
    if date_first > date_second:
        return False, 'From_date cannot bigger than to_date'
    try:
        orders = OrderSchema.objects.filter(created_date__range=[date_first, date_second])
        return True, orders
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]


def get_order_not_deliver() -> Tuple[bool, Union[str, List[OrderSchema]]]:
    try:
        orders = OrderSchema.objects.filter(status__id=2)
        return orders
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]


def get_history_order_by_user(username) -> Tuple[bool, Union[str, List[OrderSchema]]]:
    try:
        orders = OrderSchema.objects.filter(username=username, status=1)
        return True, orders
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]


def get_order_by_shipper(shipper) -> Tuple[bool, Union[str, List[OrderSchema]]]:
    try:
        orders = OrderSchema.objects.filter(username=shipper, status__id__range=[2, 4])
        return True,orders
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
