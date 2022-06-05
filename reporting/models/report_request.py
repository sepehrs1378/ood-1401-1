from django.utils.timezone import now
from django.db import models
from users.models.manager import Manager
from django.utils.translation import gettext as _


class ReportType(models.TextChoices):
    """
    Type of report request, based on requirements
    """

    REQUESTS_WITH_NEGATIVE_FEEDBACK = "REQUESTS_WITH_NEGATIVE_FEEDBACK", _(
        "Requests with customer's negative feedback"
    )
    CANCELED_REQUESTS = "CANCELED_REQUESTS", _("Requests that have been canceled")
    EXPERTS = "EXPERTS", _("List of experts")
    SERVICES = "SERVICES", _("List of services")
    SERVICE_CATEGORIES = "SERVICE_CATEGORIES", _("List of service categories")
    FEEDBACKS = "FEEDBACKS", _("List of feedbacks")


class ReportSortType(models.TextChoices):
    """
    Determines the way to sort request result list
    """

    BY_RATING = "BY_RATING", _("Sort by rating")
    BY_POPULARITY = "BY_POPULARITY", _("Sort by popularity")
    NO_SORTING = "NO_SORTING", _("Without sorting")


class ReportRequest(models.Model):
    """
    A report request sent from a manager
    """

    start_time = models.DateField(blank=False, null=False)
    end_time = models.DateField(default=now)
    report_type = models.CharField(
        max_length=40, choices=ReportType.choices, null=False, blank=False
    )
    report_sort_type = models.CharField(
        max_length=40, choices=ReportSortType.choices, default=ReportSortType.NO_SORTING
    )
    request_initiator = models.ForeignKey(Manager, on_delete=models.CASCADE)
