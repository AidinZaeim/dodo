from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50,null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    job = models.CharField(max_length=255,null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True