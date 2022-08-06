from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _

from .ticket import Ticket
from users.models.user import User


class TicketMessage(models.Model):
    """
    A single message sent in a ticket
    A ticket may have multiple messages
    """

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )
    text = models.TextField()
    file = models.FileField()
    time = models.DateField(default=now)
    sender = models.ForeignKey(
        User,
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"message: {self.text}"
