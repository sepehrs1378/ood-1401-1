from django.db import models
from django.utils.timezone import now

from .channel import Channel
from services.models.service_request import ServiceRequest
from users.models import User


class Message(models.Model):
    """
    A single message within a Message channel
    """

    channel = models.ForeignKey(
        Channel,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    sender = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    time = models.DateField(default=now)
