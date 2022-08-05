from django.urls import path
from django.conf.urls import include
from star_ratings.models import Rating
from home_service.dependency_injection import dependency_injector

app_name = "feedback"
feedback_view = dependency_injector.feedback_view

urlpatterns = [
    path("rate", include('star_ratings.urls', namespace='ratings'), name='ratings')
]
