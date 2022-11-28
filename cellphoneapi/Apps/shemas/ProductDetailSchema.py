from django.db import models


class ProductDetail(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', verbose_name='Id')
    os_system = models.CharField(db_column='os_system', verbose_name='Os_System', blank=True, null=True, max_length=30)
    battery = models.CharField(db_column='battery', verbose_name='Battery', blank=True, null=True, max_length=30)
    resolution = models.CharField(db_column='resolution', verbose_name='Resolution', blank=True, null=True,
                                  max_length=30)
    camera_behind = models.CharField(db_column='camera_behind', verbose_name='Camera_Behind', blank=True, null=True,
                                     max_length=100)
    camera_front = models.CharField(db_column='camera_front', verbose_name='Camera_Front', blank=True, null=True,
                                    max_length=100)

    ram_storage = models.CharField(db_column='ram_storage', verbose_name='Ram_Storage', blank=True, null=True,
                                   max_length=10)

    memory_card = models.CharField(db_column='memory_card', verbose_name='Memory_Cart', blank=True, null=True,
                                   max_length=10)
    chipset = models.CharField(db_column='chip_set', verbose_name='Chip_Set', blank=True, null=True, max_length=30)

    class Meta:
        db_table = 'product_detail'