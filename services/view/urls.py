from django.urls import path
from .views import *

app_name = "services"

urlpatterns = [
    path("request", request_service, name="request_service"),
    path("approve/<int:request_id>", approve_request, name="approve_request"),
    path("finish/<int:request_id>", finish_request, name="finish_request"),
]
