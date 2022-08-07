from django.utils.timezone import now
from django.db import models
from services.models.service_request import ServiceRequest


class Feedback(models.Model):
    """
    Complete customer feedback result from a service request
    'EvaluationFeedback' has relation with this class
    """

    service_request = models.ForeignKey(
        ServiceRequest, on_delete=models.CASCADE, blank=False, null=False
    )
    time_of_completion = models.DateField(default=now)

    # other opinions of the customer (also when request is canceled)
    customer_description = models.TextField()

    def __str__(self) -> str:
        return f"{self.service_request} - {self.time_of_completion} - {self.customer_description}"
