from django import forms
from django.contrib.contenttypes.fields import GenericRelation
from feedback.models.feedback import Feedback
from star_ratings.models import Rating

class FeedbackForm(forms.ModelForm):

    name = forms.CharField(max_length = 140)
    ratings = GenericRelation(Rating, related_query_name='foos')

    def __str__(self):
        return self.name

    class Meta:
        model = Feedback
        fields = (
            "service_request",
            "time_of_completion",
            "customer_description",)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)