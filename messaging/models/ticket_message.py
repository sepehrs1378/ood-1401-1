from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _

from .ticket_channel import TicketChannel
from users.models.user import User


class TicketMessage(models.Model):
    """
    A single message sent in a ticket
    A ticket may have multiple messages
    """

    ticket = models.ForeignKey(
        TicketChannel, on_delete=models.CASCADE, blank=False, null=False
    )
    text = models.TextField()
    sender = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    time = models.DateField(default=now)

    def __str__(self) -> str:
        return f"message: {self.text}"
