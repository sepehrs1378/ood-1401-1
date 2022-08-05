from django.urls import path
from .views import *

app_name = "feedback"
feedback_view = FeedbackView()

urlpatterns = [
    path(
        "send/<int:request_id>",
        feedback_view.send_feedback,
        name="request_service_from_expert",
    ),
]
