# Generated by Django 4.1.2 on 2022-11-02 10:20

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0002_cart_product_color_product_height_product_image_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatusSchema',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='Id')),
                ('status_name', models.CharField(blank=True, db_column='status_name', max_length=10, null=True, verbose_name='Status_Name')),
            ],
            options={
                'db_table': 'order_status',
            },
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
