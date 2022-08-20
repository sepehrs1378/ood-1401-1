from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models.customer import Customer
from users.models.expert import Expert
from users.models.manager import Manager
from users.models.it_manager import ITManager
from users.models.role import Role


class User(AbstractUser):
    """
    This class represents an Abstract User in our system
    """

    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=11)
    name = models.CharField(max_length=50, blank=False, null=False, default="no name")
    avatar = models.ImageField(upload_to="images/", blank=True, null=True)
    role = models.ForeignKey(
        Role,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        default=None,
    )

    def get_user_type_str(self) -> str:
        user_type = None
        if isinstance(self.role, Expert):
            user_type = "expert"
        elif isinstance(self.role, Customer):
            user_type = "customer"
        elif isinstance(self.role, Manager):
            user_type = "manager"
        elif isinstance(self.role, ITManager):
            user_type = "it_manager"
        return user_type

    def __str__(self):
        return "{}-{}".format(self.username, self.name)
