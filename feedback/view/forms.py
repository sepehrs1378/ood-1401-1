from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

import feedback
from feedback.models.evaluation_feedback import EvaluationFeedback
from feedback.models.evaluation_metric import EvaluationMetric
from feedback.models.feedback import Feedback
from services.models.service_request import ServiceRequest


RATE_CHOICES = [
    ("0", 0),
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
]


class FeedbackForm(forms.Form):
    description = forms.CharField(
        label="",
        strip=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "سایر توضیحات",
                "style": "text-align: right; direction: rtl; width: 100%",
            }
        ),
        help_text=None,
    )

    def __init__(self, metrics, request_id, request=None, **kwargs):
        super(FeedbackForm, self).__init__(request, **kwargs)

        self.fields["description"].required = False
        self.metrics = metrics
        self.request_id = request_id

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                "description",
                css_class="w-100",
            )
        )

        for index, metric in enumerate(metrics):
            self.fields[f"metric-{index}"] = forms.ChoiceField(
                choices=RATE_CHOICES, widget=forms.RadioSelect
            )
            self.fields[f"metric-{index}"].help_text = None
            self.fields[f"metric-{index}"].label = metric.question
            self.fields[f"metric-{index}"].initial = "0"
            self.helper.layout.fields.append(
                Div(
                    f"metric-{index}",
                    css_class="metric-entry",
                    css_id=f"metric-{index}",
                ),
            )

        self.helper.layout.fields.append(
            Submit(
                "submit",
                "ثبت نظر",
                css_class="btn btn-dark py-2 mt-2",
            ),
        )

    def save(self):
        service_request = ServiceRequest.objects.filter(pk=self.request_id).first()
        feedback = Feedback.objects.create(
            service_request=service_request,
            customer_description=self.cleaned_data["description"],
        )
        for index, metric in enumerate(self.metrics):
            evaluation_feedback = EvaluationFeedback.objects.create(
                rate=int(self.cleaned_data[f"metric-{index}"]),
                evaluation_metric=metric,
                feedback=feedback,
            )
        return feedback
