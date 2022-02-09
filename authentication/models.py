from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password):
        validate_email(email)
        validate_password(password)
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    AUTHOR = 'Aut'
    SUBSCRIBER = 'Sub'
    RoleChoice = (
        (AUTHOR, 'Author'),
        (SUBSCRIBER, 'Subscriber'),
    )

    username = models.CharField(db_index=True, max_length=255, unique=True, null=True)
    email = models.EmailField(db_index=True, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=3, choices=RoleChoice, default=SUBSCRIBER)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
