from django import template

from services.models.service_request import RequestStatus

register = template.Library()


@register.filter(name="get_css_class")
def get_css_class(value):
    if value == RequestStatus.CANCELED_BY_CUSTOMER:
        return "danger"
    if value == RequestStatus.EXPERT_FOUND:
        return "success"
    if value == RequestStatus.FINDING_EXPERT:
        return "info"
    if value == RequestStatus.FEEDBACK_RECEIVED:
        return "success"
    if value == RequestStatus.NO_EXPERT_FOUND:
        return "danger"
    if value == RequestStatus.SENT_TO_EXPERT:
        return "secondary"
    if value == RequestStatus.WAIT_FOR_EXPERT_APPROVAL:
        return "secondary"
    if value == RequestStatus.FINISHED:
        return "dark"
    if value == RequestStatus.IN_PROGRESS:
        return "primary"
    if value == RequestStatus.REJECTED_BY_EXPERT:
        return "danger"
    return "primary"
