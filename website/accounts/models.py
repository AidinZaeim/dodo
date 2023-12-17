from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import *
from django.utils import timezone
# ----------------------------------------------------------------------------------------------------------------------------
class User(AbstractBaseUser):
    """
        main User object that extends django-user
        username --> email

    """
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=255,null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='users/',default ='users/image.jpg')

    can_change_password = models.BooleanField(default=False)
    code = models.IntegerField(blank=True,null=True)

    # REQUIRED_FIELDS = ['nationalCode']
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return str(self.email) + " - " + str(self.firstName) + " " + str(self.lastName)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin
# ----------------------------------------------------------------------------------------------------------------------------