from turtle import ondrag
from django.db import models
from .evaluation_metric import EvaluationMetric
from .feedback import Feedback
from django.core.validators import MaxValueValidator, MinValueValidator


class EvaluationFeedback(models.Model):
    """
    A single feedback rating to a single evaluation question
    """

    rate = models.IntegerField(
        blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    evaluation_metric = models.ForeignKey(
        EvaluationMetric, blank=False, null=False, on_delete=models.CASCADE
    )
    feedback = models.ForeignKey(
        Feedback, blank=False, null=False, on_delete=models.CASCADE
    )
