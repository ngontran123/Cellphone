# Generated by Django 4.1.2 on 2022-11-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0004_alter_orderstatusschema_status_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='username',
            field=models.CharField(blank=True, db_column='username', max_length=100, null=True, verbose_name='Username'),
        ),
    ]
