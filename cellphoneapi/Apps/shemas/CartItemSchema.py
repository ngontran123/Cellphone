from django.db import models
from ..shemas.CartSchema import Cart
from ..shemas.ProductSchema import Product


class CartItem(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Id', db_column='id')
    pd = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    price = models.FloatField(db_column='price', null=True, blank=True, verbose_name='Price')
    weight = models.FloatField(db_column='weight', null=True, blank=True, verbose_name='Weight')
    quantity = models.IntegerField(db_column='quantity', null=True, blank=True, verbose_name='Quantity')
    product_name = models.CharField(db_column='product_name', null=True, blank=True, verbose_name='Product_Name',
                                    max_length=200)

    class Meta:
        db_table = 'cart_item'

