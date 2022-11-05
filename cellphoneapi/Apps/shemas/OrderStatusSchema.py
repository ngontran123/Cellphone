from django.db import models


class OrderStatusSchema(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', verbose_name='Id')
    status_name = models.CharField(db_column='status_name', verbose_name='Status_Name', blank=True, null=True,
                                   max_length=30)

    class Meta:
        db_table = 'order_status'
