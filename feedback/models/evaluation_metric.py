from django.db import models


class EvaluationMetric(models.Model):
    """
    A single question, used for customer feedback
    """

    question = models.TextField(blank=False, null=False)
    hidden = models.BooleanField(default=False)
