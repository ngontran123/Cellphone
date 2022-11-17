import math

from ..shemas.ProductSchema import Product
from ..constants.error_code import ErrorCode, MSG_TEMPLATE
from typing import Tuple, List, Union
from ..shemas.ProductDetailSchema import ProductDetail
from ..serializers.ProductSerializer import ProductSerializer


def get_all_product() -> Tuple[bool, Union[str, Product]]:
    try:
        products = Product.objects.all()
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, products


def get_product_by_id(product_id) -> Tuple[bool, Union[str, Product]]:
    try:
        product = Product.objects.get(id=product_id)
        if not product:
            return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, product


def add_product(request):
    new_product = {
        'brand': request['brand'],
        'name': request['name'],
        'description': request['description'],
        'price': request['price'],
        'status': request['status'],
        'width': request['width'],
        'weight': request['weight'],
        'height': request['height'],
        'image_url': request['image_url'],
        'pd_detail': request['pd_detail']

    }
    return new_product


def get_product_by_name(name) -> Tuple[bool, Union[str, Product]]:
    try:
        product = Product.objects.filter(name__icontains=name)
        if not product:
            return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, product


def get_product_by_brand(brand) -> Tuple[bool, Union[str, Product]]:
    try:
        product = Product.objects.filter(brand__icontains=brand)
        if not product:
            return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]
    return True, product


def get_product_between_price(from_price, to_price) -> Tuple[bool, Union[str, Product]]:
    try:
        from_price = float(from_price)
        to_price = float(to_price)
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.UNHANDLE_EXCEPTION]
    if from_price < 0 or to_price < 0:
        return False, 'Money cannot have negative value'
    if from_price > to_price:
        return False, 'From_price cannot bigger than to_price'
    products = Product.objects.filter(price__range=(from_price, to_price))
    return True, products


def pagination(page, lim):
    try:
        lim = int(lim)
        page = int(page)
        skip = (page - 1) * lim
        if page < 0 or lim < 0:
            return False, 'Cannot have negative value'
        products = Product.objects.all()
        products_skip = products[skip:skip + lim]
        dict_products = {}
        products_serial = ProductSerializer(products_skip, many=True)
        dict_products['products'] = products_serial.data
        dict_products['page'] = math.ceil(len(products) / lim)
        return True, dict_products
    except Exception as e:
        return False, 'Cannot paginating'


def check_out_of_stock(status) -> Tuple[bool, Union[str, Product]]:
    products = Product.objects.filter(status=status)
    if not products:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, products


def get_product_detail_by_id(id) -> Tuple[bool, Union[str, ProductDetail]]:
    product_detail = ProductDetail.objects.filter(id=id).first()
    if not product_detail:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, product_detail
