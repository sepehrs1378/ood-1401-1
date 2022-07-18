from dataclasses import field
from django import forms

from services.models.service_request import RequestType, ServiceRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Div, Field, Column
from services.models.service import Service
from users.models.expert import Expert


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ["expert", "service", "request_type", "customer"]

    def __init__(self, *args, **kwargs):
        super(ServiceRequestForm, self).__init__(*args, **kwargs)
        self.fields["customer"].widget.attrs["readonly"] = True
        self.fields["request_type"].widget.attrs["readonly"] = True
        self.fields["service"].widget.attrs["placeholder"] = "انتخاب سرویس"
        self.fields["service"].label = "سرویس"
        self.fields["service"].help_text = None
        expert = Expert.objects.filter(pk=kwargs["initial"]["expert"]).first()
        self.fields["service"].queryset = Service.objects.filter(pk=expert.expertise.id)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                "service",
                css_class="container complete-rtl px-0 mx-0",
            ),
            Submit(
                "submit",
                "ثبت درخواست",
                css_class="btn btn-dark py-2 mt-2",
            ),
        )


class ServiceRequestFromSystemForm(forms.Form):
    service = forms.ModelChoiceField(queryset=Service.objects.all())

    class Meta:
        fields = ["service"]

    def __init__(self, *args, **kwargs):
        super(ServiceRequestFromSystemForm, self).__init__(*args, **kwargs)
        self.fields["service"].label = "سرویس انتخاب شده"
        self.fields["service"].disabled = True

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                "service",
                css_class="container complete-rtl px-0 mx-0",
            ),
            Submit(
                "submit",
                "ارسال درخواست",
                css_class="btn btn-dark py-2 mt-2",
            ),
        )

    def save(self):
        # TODO
        return ServiceRequest.objects.first()
