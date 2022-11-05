from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy


class CustomeUserService(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email cannot be null")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
