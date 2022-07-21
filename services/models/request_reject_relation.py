from django.db import models
from services.models.service_request import ServiceRequest

from users.models.user import User


class RequestRejectionRelation(models.Model):
    """
    This relation is used to keep a record of experts that rejected a request
    """

    expert = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="relation_expert",
    )

    request = models.ForeignKey(
        ServiceRequest,
        on_delete=models.CASCADE,
        related_name="relation_request",
    )
