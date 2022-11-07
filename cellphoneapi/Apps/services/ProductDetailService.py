from ..shemas.ProductDetailSchema import ProductDetail
from ..constants.error_code import ErrorCode, MSG_TEMPLATE
from typing import Tuple, List, Union


def get_product_detail() -> Tuple[bool, Union[str, List[ProductDetail]]]:
    try:
        pd_details = ProductDetail.objects.all()
        return True, pd_details
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]


def get_product_detail_by_id(id) -> Tuple[bool, Union[str, ProductDetail]]:
    pd_detail = ProductDetail.objects.filter(id=id).first()
    if not pd_detail:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, pd_detail


