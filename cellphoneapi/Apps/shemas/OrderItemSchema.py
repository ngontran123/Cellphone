from django.db import models
from ..shemas.OrderSchema import OrderSchema
from ..shemas.ProductSchema import Product


class OrderItemSchema(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', verbose_name='Id')
    pd = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderSchema, on_delete=models.CASCADE)
    price = models.FloatField(db_column='price', blank=True, null=True, verbose_name='Price')
    weight = models.FloatField(db_column='weight', blank=True, null=True, verbose_name='Weight')
    product_name = models.CharField(db_column='product_name', blank=True, null=True, verbose_name='Product_Name',
                                    max_length=200)
    quantity = models.IntegerField(db_column='quantity', blank=True, null=True, verbose_name='Quantity')

    class Meta:
        db_table = 'order_item'
