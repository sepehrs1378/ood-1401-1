from django.db import models
from users.models import Customer, Expert, User
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


class Message(models.Model):
    """
    A single message within a Message channel
    """

    channel = models.ForeignKey(
        Channel, blank=False, null=False, on_delete=models.CASCADE
    )
    sender = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    time = models.DateField(default=now)
    text = models.TextField()
    # TODO: is file needed??
    # file = models.FileField()
