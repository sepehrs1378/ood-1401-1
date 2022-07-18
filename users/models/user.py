import re
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    This class represents an Abstract User in our system
    """

    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=10)
    name = models.CharField(max_length=50, blank=False, null=False, default="no name")

    class Meta:
        abstract = False  # one-to-one relationship from children to parent

    def __str__(self):
        return "{}".format(self.username)
