from django.db import models
from services.models.service import Service
from django.utils.translation import gettext as _

from users.models.user import User


class RequestStatus(models.TextChoices):
    """
    Statues of a service request
    wether the customer requested service from a specific expert or expert is selected by system
    """

    INITIATED = "INITIATED", _("ساخته شده")
    FINDING_EXPERT = "FINDING_EXPERT", _("در حال پیدا کردن متخصص")
    EXPERT_FOUND = "EXPERT_FOUND", _("متخصص پیدا شد")
    NO_EXPERT_FOUND = "NO_EXPERT_FOUND", _("هیچ متخصصی پیدا نشد")
    WAIT_FOR_EXPERT_APPROVAL = "WAIT_FOR_EXPERT_APPROVAL", _("منتظر تایید متخصص")
    SENT_TO_EXPERT = "SENT_TO_EXPERT", _("درخواست به متخصص ارسال شد")
    IN_PROGRESS = "IN_PROGRESS", _("درخواست در حال انجام است")
    FINISHED = "FINISHED", _("درخواست به پایان رسیده است")
    PAYMENT_DONE = "PAYMENT_DONE", _("پرداخت انجام شده")
    CANCELED_BY_CUSTOMER = "CANCELED_BY_CUSTOMER", _("از طرف مشتری لغو شد")
    REJECTED_BY_EXPERT = "CANCELED_BY_EXPERT", _("متخصص درخواست را رد کرد")
    FEEDBACK_RECEIVED = "FEEDBACK_RECEIVED", _("بازخورد دریافت شد")


class RequestType(models.TextChoices):
    """
    Type of Service Request
    """

    CUSTOMER_SELECTED = "CUSTOMER_SELECTED", _("متخصص توسط مشتری انتخاب شده است")
    SYSTEM_SELECTED = "SYSTEM_SELECTED", _("متخصص توسط سیستم پیشنهاد داده شده است")


class ServiceRequest(models.Model):
    """
    A service request from customer,
    wether a specific expert is selected, or system suggested the experts
    """

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="service_customer",
    )
    expert = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="service_expert",
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=30,
        choices=RequestStatus.choices,
        default=RequestStatus.INITIATED,
    )
    request_type = models.CharField(
        max_length=30,
        choices=RequestType.choices,
        default=RequestType.SYSTEM_SELECTED,
    )
    service = models.ForeignKey(
        Service,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="requests",
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"\nrequest: {self.service} |\nfrom: {self.customer} |\nexpert: {self.expert} |\nstatus: {self.status} \t"
