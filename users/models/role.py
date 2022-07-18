from django.db import models
from polymorphic.models import PolymorphicModel


class Role(PolymorphicModel):
    """
    Identifies the role of each user in system
    """

    name = models.CharField(max_length=20, default="Role")
