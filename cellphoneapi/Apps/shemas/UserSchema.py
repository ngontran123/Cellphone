from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractUser
class UserSchema(AbstractUser):
    id=models.AutoField(primary_key=True,db_column='id',verbose_name='Id')
    username=models.CharField(max_length=100,db_column='username',null=True,blank=True,verbose_name='Username'),
    email=models.EmailField(gettext_lazy('email_address'),verbose_name='Email',db_column='email',unique=True),
    password=models.CharField()