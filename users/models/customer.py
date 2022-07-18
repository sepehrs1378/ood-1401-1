from users.models.role import Role
from django.db import models


class Customer(Role):
    """
    A Customer is a User who wants to get services
    """

    address = models.TextField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
