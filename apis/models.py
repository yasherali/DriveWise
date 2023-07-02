from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from rest_framework.authtoken.models import Token
from django.utils.crypto import get_random_string

# Create your models here.


class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    is_active = None
    last_login = None
    date_joined = None
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    USERNAME_FIELD = 'email'

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'  # add a unique related_name attribute
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups'  # add a unique related_name attribute
    )

    def __str__(self):
        return self.email


class CustomUserToken(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate a unique key for the token
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        # Generate a unique key for the token
        return get_random_string(length=40)

    def __str__(self):
        return self.key
