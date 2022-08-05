from django.db import models


class EvaluationMetric(models.Model):
    """
    A single question, used for customer feedback
    """

    question = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.question}"
