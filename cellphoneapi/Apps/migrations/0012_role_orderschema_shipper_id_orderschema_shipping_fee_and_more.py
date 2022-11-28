# Generated by Django 4.1.2 on 2022-11-07 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0011_alter_productdetail_camera_behind_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='Id')),
                ('role_name', models.CharField(blank=True, db_column='role_name', max_length=30, null=True, verbose_name='Role_Name')),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.AddField(
            model_name='orderschema',
            name='shipper_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderschema',
            name='shipping_fee',
            field=models.FloatField(blank=True, db_column='shipping_fee', null=True, verbose_name='Shipping_Fee'),
        ),
        migrations.AddField(
            model_name='user',
            name='car_id',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Apps.role'),
        ),
    ]