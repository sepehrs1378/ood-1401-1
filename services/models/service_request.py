from django.db import models
from users.models.customer import Customer
from users.models.expert import Expert
from services.models.service import Service
from django.utils.translation import gettext as _


class RequestStatus(models.TextChoices):
    """
    Statues of a service request
    wether the customer requested service from a specific expert or expert is selected by system
    """

    INITIATED = "INITIATED", _("Initiated")
    FINDING_EXPERT = "FINDING_EXPERT", _("Finding expert")
    EXPERT_FOUND = "EXPERT_FOUND", _("Expert found")
    NO_EXPERT_FOUND = "NO_EXPERT_FOUND", _("No experts found")
    WAIT_FOR_EXPERT_APPROVAL = "WAIT_FOR_EXPERT_APPROVAL", _(
        "Waiting for expert to approve"
    )
    SENT_TO_EXPERT = "SENT_TO_EXPERT", _("Request sent to expert")
    IN_PROGRESS = "IN_PROGRESS", _("Request is in progress")
    FINISHED = "FINISHED", _("Request is finsihed")
    PAYMENT_DONE = "PAYMENT_DONE", _("Payment done")
    CANCELED_BY_CUSTOMER = "CANCELED_BY_CUSTOMER", _("Request canceled by customer")
    CANCELED_BY_EXPERT = "CANCELED_BY_EXPERT", _("Request canceled by expert")
    FEEDBACK_RECEIVED = "FEEDBACK_RECEIVED", _("Feedback received")


class RequestType(models.TextChoices):
    """
    Type of Service Request
    """

    CUSTOMER_SELECTED = "CUSTOMER_SELECTED", _("Customer selects a specific expert")
    SYSTEM_SELECTED = "SYSTEM_SELECTED", _("System recommends the service")


class ServiceRequest(models.Model):
    """
    A service request from customer,
    wether a specific expert is selected, or system suggested the experts
    """

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=False, null=False
    )
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=30, choices=RequestStatus.choices, default=RequestStatus.INITIATED
    )
    request_type = models.CharField(
        max_length=30, choices=RequestType.choices, default=RequestType.SYSTEM_SELECTED
    )
    service = models.ForeignKey(
        Service, blank=False, null=False, on_delete=models.CASCADE
    )
