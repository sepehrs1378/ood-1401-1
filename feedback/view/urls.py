from django.urls import path
from .views import *

app_name = "feedback"
feedback_view = FeedbackView()

urlpatterns = [
    path(
        "send/<int:request_id>",
        feedback_view.send_feedback,
        name="feedback_send",
    ),
    path(
        "get/<int:request_id>",
        feedback_view.get_feedback,
        name="feedback_get",
    ),
    path(
        "metrics",
        feedback_view.metrics_list,
        name="list_metrics"
    ),
    path("metric/<int:metric_id>",
         feedback_view.metric,
         name="metric_update")
]
