# Generated by Django 4.1.2 on 2022-11-05 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0008_orderschema'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='Id')),
                ('os_system', models.CharField(blank=True, db_column='os_system', max_length=30, null=True, verbose_name='Os_System')),
                ('battery', models.CharField(blank=True, db_column='battery', max_length=30, null=True, verbose_name='Battery')),
                ('resolution', models.CharField(blank=True, db_column='resolution', max_length=30, null=True, verbose_name='Resolution')),
                ('camera_behind', models.CharField(blank=True, db_column='camera_behind', max_length=30, null=True, verbose_name='Camera_Behind')),
                ('camera_front', models.CharField(blank=True, db_column='camera_front', max_length=30, null=True, verbose_name='Camera_Front')),
                ('ram_storage', models.CharField(blank=True, db_column='ram_storage', max_length=10, null=True, verbose_name='Ram_Storage')),
                ('memory_card', models.CharField(blank=True, db_column='memory_card', max_length=10, null=True, verbose_name='Memory_Cart')),
                ('chipset', models.CharField(blank=True, db_column='chip_set', max_length=30, null=True, verbose_name='Chip_Set')),
            ],
            options={
                'db_table': 'product_detail',
            },
        ),
        migrations.CreateModel(
            name='OrderItemSchema',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='Id')),
                ('price', models.FloatField(blank=True, db_column='price', null=True, verbose_name='Price')),
                ('weight', models.FloatField(blank=True, db_column='weight', null=True, verbose_name='Weight')),
                ('product_name', models.CharField(blank=True, db_column='product_name', max_length=200, null=True, verbose_name='Product_Name')),
                ('quantity', models.IntegerField(blank=True, db_column='quantity', null=True, verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.orderschema')),
                ('pd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.product')),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
    ]
