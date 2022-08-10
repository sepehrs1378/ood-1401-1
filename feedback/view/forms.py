from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

import feedback
from feedback.models.evaluation_feedback import EvaluationFeedback
from feedback.models.evaluation_metric import EvaluationMetric
from feedback.models.feedback import Feedback
from services.models.service_request import RequestStatus, ServiceRequest

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

    def __init__(self, metrics, request_id, is_editable, request=None, **kwargs):
        super(FeedbackForm, self).__init__(request, **kwargs)

        self.fields["description"].required = False
        self.metrics = metrics
        self.request_id = request_id

        self.helper = FormHelper(self)
        self.helper.layout = Layout()

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
                    css_class="metric-entry" if is_editable else "",
                    css_id=f"metric-{index}",
                ),
            )
        self.helper.layout.fields.append(
            Div(
                "description",
                css_class="w-100",
            )
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
            EvaluationFeedback.objects.create(
                rate=int(self.cleaned_data[f"metric-{index}"]),
                evaluation_metric=metric,
                feedback=feedback,
            )
        service_request.status = RequestStatus.FEEDBACK_RECEIVED
        service_request.save()
        return feedback

    def initiate_from_feedback(self):
        service_request = ServiceRequest.objects.filter(pk=self.request_id).first()
        feedback = Feedback.objects.filter(service_request=service_request).first()

        for index, rate in enumerate(feedback.feedbacks.all()):
            self.fields[f"metric-{index}"].initial = str(rate.rate)

        self.fields["description"].initial = feedback.customer_description

        for field in self.fields.keys():
            self.fields[field].disabled = True

        self.helper.layout.fields = self.helper.layout.fields[:-1]


class MetricForm(forms.ModelForm):
    class Meta:
        model = EvaluationMetric
        fields = ['question']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__( *args, **kwargs)
        self.fields["question"].label = "سوال"

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div("question", css_class="col"),
            Submit(
                "ُSave",
                "ذخیره",
                css_class="btn btn-dark py-2 mt-2",
                style="width: 10%",
            ))
