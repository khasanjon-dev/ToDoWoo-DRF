from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models import (BooleanField, DateTimeField, CharField, EmailField)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = CharField(max_length=150, unique=True, validators=[username_validator])
    email = EmailField(null=True, blank=True)

    # permissions
    is_superuser = BooleanField(default=False)
    is_staff = BooleanField(default=False)
    # date
    updated_at = DateTimeField(auto_now=True, null=True)
    created_at = DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
