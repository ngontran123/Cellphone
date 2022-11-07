from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy
from .shemas.RoleSchema import Role


class User(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)
    email = models.EmailField(gettext_lazy('email_address'), unique=True)
    phone = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=30, unique=True, blank=True, null=True)
    car_id = models.CharField(max_length=30, unique=True, blank=True, null=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
