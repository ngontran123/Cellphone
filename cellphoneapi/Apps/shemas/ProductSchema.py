from django.db import models
from ..shemas.ProductDetailSchema import ProductDetail


class Product(models.Model):
    id = models.AutoField(primary_key=True, db_column="Id", verbose_name='Id')
    brand = models.CharField(db_column='brand', blank=True, null=True, verbose_name='Brand', max_length=30)
    name = models.CharField(db_column='name', blank=True, null=True, verbose_name='Name', max_length=30)
    description = models.CharField(db_column='description', blank=True, null=True, verbose_name='Description',
                                   max_length=100)
    price = models.FloatField(db_column='price', blank=True, null=True, verbose_name='Price')
    status = models.CharField(db_column='status', blank=True, null=True, verbose_name='Status', max_length=10)
    width = models.IntegerField(db_column='width', blank=True, null=True, verbose_name='Width')
    height = models.IntegerField(db_column='height', blank=True, null=True, verbose_name='Height')
    image_url = models.CharField(db_column='image_url', blank=True, null=True, verbose_name='Image_Url', max_length=200)
    weight = models.FloatField(db_column='weight', blank=True, null=True, verbose_name='Weight')
    pd_detail = models.ForeignKey(ProductDetail, on_delete=models.CASCADE, unique=True, null=True, blank=True)

    class Meta:
        db_table = 'product'
