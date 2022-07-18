from django.urls import path
from .views import *

app_name = "services"
service_catalogue = ServiceCatalogue()

urlpatterns = [
    path(
        "request/<int:expert_id>",
        service_catalogue.request_service_from_expert,
        name="request_service_from_expert",
    ),
    path(
        "request",
        service_catalogue.request_service_from_system,
        name="request_service_from_system",
    ),
    path(
        "approve/<int:request_id>",
        service_catalogue.approve_request,
        name="approve_request",
    ),
    path(
        "finish/<int:request_id>",
        service_catalogue.finish_request,
        name="finish_request",
    ),
    path("experts/list", service_catalogue.experts_list, name="experts_list"),
    path(
        "request/finding/<int:service_request_id>",
        service_catalogue.finding_expert,
        name="finding_expert",
    ),
]
