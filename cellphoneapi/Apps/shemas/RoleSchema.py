from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', verbose_name='Id')
    role_name = models.CharField(db_column='role_name', verbose_name='Role_Name', blank=True, null=True, max_length=30)

    class Meta:
        db_table = 'role'

        
