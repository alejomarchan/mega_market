from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import CharField, EmailField, DateTimeField, BooleanField

# Create your models here.

class My_Account_Manager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password=password,
        )
    
        user.is_superadmin = True
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    username = CharField(max_length=50, unique=True)
    email = EmailField(max_length=100, unique=True)
    phone_number = CharField(max_length=50)

    #Required
    date_joined = DateTimeField(auto_now_add=True)
    last_login = DateTimeField(auto_now_add=True)
    is_superadmin = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    object = My_Account_Manager()

    def __str__(self):
        return self.email

    def has_perm(self, permiso, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True