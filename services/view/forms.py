from django import forms

from services.models.service_request import RequestType, ServiceRequest


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ["expert", "service", "request_type", "customer"]

    def __init__(self, *args, **kwargs):
        super(ServiceRequestForm, self).__init__(*args, **kwargs)
        self.fields["customer"].widget.attrs["readonly"] = True
        self.fields["request_type"].widget.attrs["readonly"] = True
