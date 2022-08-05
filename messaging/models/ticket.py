from django.db import models
from users.models.user import User
from django.utils.timezone import now
from django.utils.translation import gettext as _


class TicketStatus(models.TextChoices):
    CREATED = "CREATED", _("Created")
    WAIT_FOR_CUSTOMER_RESPONSE = "WAIT_FOR_CUSTOMER_RESPONSE", _(
        "Waiting for customer response"
    )
    WAIT_FOR_ADMIN_RESPONSE = "WAIT_FOR_ADMIN_RESPONSE", _("Wait for admin response")
    FINISHED = "FINISHED", _("Finished")


class Ticket(models.Model):
    """
    A Ticket that is created by customer or expert
    """

    creator = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )  # to avoid inheritance problems, we use pk of user
    topic = models.CharField(max_length=30)
    time_of_creation = models.DateField(default=now)
    status = models.CharField(
        max_length=30, choices=TicketStatus.choices, default=TicketStatus.CREATED
    )

    def __str__(self) -> str:
        return f"Topic: {self.topic} | status: {self.status}"
