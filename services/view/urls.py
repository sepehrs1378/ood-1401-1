from django.urls import path
from .views import *

app_name = "services"
service_view = ServiceView()

urlpatterns = [
    path(
        "request/<int:expert_id>",
        service_view.request_service_from_expert,
        name="request_service_from_expert",
    ),
    path(
        "request",
        service_view.request_service_from_system,
        name="request_service_from_system",
    ),
    path(
        "approve/<int:request_id>",
        service_view.approve_request,
        name="approve_request",
    ),
    path(
        "reject/<int:request_id>",
        service_view.reject_request,
        name="reject_request",
    ),
    path(
        "accept-expert/<int:request_id>",
        service_view.accept_expert,
        name="reject_request",
    ),
    path(
        "finish/<int:request_id>",
        service_view.finish_request,
        name="finish_request",
    ),
    path("experts/list", service_view.experts_list, name="experts_list"),
    path(
        "request/finding",
        service_view.finding_expert,
        name="finding_expert",
    ),
]
