from django.db import models

from services.models.service_category import ServiceCategory


class Service(models.Model):
    """
    This class represents every service that an expert can provide
    """

    name = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField()
    category = models.ForeignKey(
        ServiceCategory, blank=False, null=False, on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f"{self.name} <-- {self.category}"
