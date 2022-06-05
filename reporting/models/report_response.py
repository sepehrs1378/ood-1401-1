from django.db import models
from .report_request import ReportRequest
from django.utils.translation import gettext as _


class ReportResponseStatus(models.TextChoices):
    SUCCESS = "SUCCESS", _("Success")
    FAILED = "FAILED", _("Failed")


class ReportResultType(models.TextChoices):
    JSON = "JSON", _("JSON")
    CSV = "CSV", _("CSV")


class ReportResponse(models.Model):
    """
    Indicates a response to a report request, the result is in binary format and will be converted in client side
    """

    request = models.ForeignKey(
        ReportRequest, blank=False, null=False, on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=30,
        choices=ReportResponseStatus.choices,
        default=ReportResponseStatus.FAILED,
    )
    result_type = models.CharField(
        max_length=30, choices=ReportResultType.choices, default=ReportResultType.CSV
    )
    result = models.BinaryField()
