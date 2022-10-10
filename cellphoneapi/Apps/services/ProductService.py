from ..shemas.ProductSchema import Product


def get_all_product():
    products = Product.objects.all()
    return products


def get_product_by_id(product_id):
    product = Product.objects.get(id=product_id)
    return product


def add_product(request):
    new_product ={
        'brand':request['brand'],
        'name':request['name'],
        'description':request['description']
    }
    return new_product
