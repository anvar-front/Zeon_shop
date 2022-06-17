from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
  AbstractBaseUser, BaseUserManager, PermissionsMixin
)

import jwt
from datetime import timedelta, datetime


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if email is None:
            raise TypeError('User must have a email!')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password):

        if email is None:
            raise TypeError('Superuser must have a username!')

        if password is None:
            raise TypeError('Superuser must have a password!')

        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    dateofadd = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    
    objects = UserManager()
