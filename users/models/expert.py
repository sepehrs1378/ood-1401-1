from services.models.service import Service
from .user import User
from django.db import models


class Expert(User):
    """
    An Expert is a User who provides services
    """

    document = models.FileField(upload_to="documents/%Y/%m/%d/", blank=True, null=True)
    expertise = models.ForeignKey(
        Service,
        blank=False,
        null=False,
        on_delete=models.PROTECT,
        default=4,
    )

    class Meta:
        verbose_name = "Expert"
        verbose_name_plural = "Experts"
