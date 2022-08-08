from services.models.service import Service
from users.models.role import Role
from django.db import models


class Expert(Role):
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
    status = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = "Expert"
        verbose_name_plural = "Experts"

    def __str__(self):
        return "متخصص"
