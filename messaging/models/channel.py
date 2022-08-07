from django.db import models
from users.models import User
from services.models.service_request import ServiceRequest
from django.utils.timezone import now


class Channel(models.Model):
    """
    A message channel between customers and experts
    Each message is related to a serivce request
    """

    customer = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE, related_name="customer"
    )
    expert = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE, related_name="expert"
    )
    related_service_request = models.ForeignKey(
        ServiceRequest, blank=False, null=False, on_delete=models.CASCADE
    )
    time_of_creation = models.DateField(default=now)

    # Returns the name of the other person on the channel
    def get_contact_name(self, your_user: User):
        if your_user.id == self.customer.id:
            return self.expert.username
        elif your_user.id == self.expert.id:
            return self.customer.id
        else:
            return False

    def __str__(self) -> str:
        return f"Customer: {self.customer_id} | Expert: {self.expert_id}"