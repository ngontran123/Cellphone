from django.db import models
from django.utils.translation import gettext_lazy
from ..shemas.OrderStatusSchema import OrderStatusSchema
from ..models import User


class OrderSchema(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', verbose_name='Id')
    username = models.CharField(db_column='username', blank=True, null=True, verbose_name='Username', max_length=100)
    created_date = models.DateTimeField(db_column='created_date', blank=True, null=True, verbose_name='Created_Date')
    updated_date = models.DateTimeField(db_column='updated_date', blank=True, null=True, verbose_name='Updated_Date')
    total_price = models.FloatField(db_column='total_price', blank=True, null=True, verbose_name='Total_Price')
    total_weight = models.FloatField(db_column='total_weight', blank=True, null=True, verbose_name='Total_Weight')
    status = models.ForeignKey(OrderStatusSchema, on_delete=models.CASCADE)
    shipping_fee = models.FloatField(db_column='shipping_fee', verbose_name='Shipping_Fee', blank=True, null=True)
    shipper_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'order'
