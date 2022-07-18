from django.urls import path
from .views import *

app_name = "services"

urlpatterns = [
    path(
        "request/<int:expert_id>",
        request_service_from_expert,
        name="request_service_from_expert",
    ),
    path("request", request_service_from_system, name="request_service_from_system"),
    path("approve/<int:request_id>", approve_request, name="approve_request"),
    path("finish/<int:request_id>", finish_request, name="finish_request"),
    path("experts/list", experts_list, name="experts_list"),
    path(
        "request/finding/<int:service_request_id>",
        finding_expert,
        name="finding_expert",
    ),
]
