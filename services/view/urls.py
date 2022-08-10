from django.urls import path
from home_service.dependency_injection import dependency_injector
from .views import *

app_name = "services"
service_view = dependency_injector.service_view

urlpatterns = [
    path(
        "request/<int:role_id>",
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
    path(
        "experts/list",
        service_view.experts_list,
        name="experts_list",
    ),
    path(
        "list",
        service_view.services_list,
        name="services_list",
    ),
    path(
        "<int:service_id>",
        service_view.service,
        name="service"
    ),
    path(
        "request/finding",
        service_view.finding_expert,
        name="finding_expert",
    ),
    path("categories",
         service_view.categories_list,
         name="categories_list"),
]
