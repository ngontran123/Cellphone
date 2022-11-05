from django.contrib import admin
from .shemas.ProductSchema import Product
from .shemas.CartSchema import Cart
admin.site.register(Product)
admin.site.register(Cart)