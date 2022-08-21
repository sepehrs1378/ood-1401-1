from django.db import models
from users.models.user import User
from django.utils.timezone import now
from django.utils.translation import gettext as _


class TicketChannel(models.Model):
    """
    A Ticket that is created by customer or expert
    """

    creator = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )  # to avoid inheritance problems, we use pk of user
    title = models.CharField(max_length=30)
    time_of_creation = models.DateField(default=now)

    # # Returns the name of the other person on the channel
    # def get_contact_name(self, your_user: User):
    #     if your_user.id == self.creator.id:
    #         return "admin"
    #     else:
    #         return self.creator.username

    def __str__(self) -> str:
        return f"Title: {self.title} | Creator: {self.creator_id}"
