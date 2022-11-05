from django.db import models


class Cart(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id',verbose_name='Id')
    username = models.CharField(db_column='username', blank=True, null=True, verbose_name='Username',max_length=100)
    created_date = models.DateTimeField(db_column='created_date', blank=True, null=True, verbose_name='Created_Date')
    updated_date = models.DateTimeField(db_column='updated_date', blank=True, null=True, verbose_name='Updated_Date')
    total_price = models.FloatField(db_column='total_price', blank=True, null=True, verbose_name='Total_Price')
    total_weight = models.FloatField(db_column='total_weight', blank=True, null=True, verbose_name='Total_Weight')

    class Meta:
        db_table = 'cart'
