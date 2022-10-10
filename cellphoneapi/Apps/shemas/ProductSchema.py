from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True, db_column="Id")
    brand = models.CharField(db_column='brand', blank=True, null=True, verbose_name='Brand', max_length=30)
    name = models.CharField(db_column='name', blank=True, null=True, verbose_name='Name', max_length=30)
    description = models.CharField(db_column='description', blank=True, null=True, verbose_name='Description',
                                   max_length=100)

    class Meta:
        db_table = 'product'
