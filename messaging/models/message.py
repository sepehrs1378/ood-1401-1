from django.db import models
from users.models import customer, expert, user
from services.models.service_request import ServiceRequest
from django.utils.timezone import now


class Message(models.Model):
    """
    A message channel between customers and experts
    Each message is related to a serivce request
    """

    customer = models.ForeignKey(
        customer.Customer, blank=False, null=False, on_delete=models.CASCADE
    )
    expert = models.ForeignKey(
        expert.Expert, blank=False, null=False, on_delete=models.CASCADE
    )
    related_service_request = models.ForeignKey(
        ServiceRequest, blank=False, null=False, on_delete=models.CASCADE
    )
    time_of_creation = models.DateField(default=now)


class MessageContent(models.Model):
    """
    A single message within a Message channel
    """

    parent_message = models.ForeignKey(
        Message, blank=False, null=False, on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        user.User, blank=False, null=False, on_delete=models.CASCADE
    )
    time = models.DateField(default=now)
    text = models.TextField()
    file = models.FileField()
