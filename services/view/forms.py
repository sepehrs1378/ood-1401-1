from dataclasses import field
from http import server
from os import stat
from django import forms

from services.models.service_request import RequestStatus, RequestType, ServiceRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Div, Field, Column
from services.models.service import Service
from users.models import customer
from users.models.expert import Expert
from users.models.user import User
from django.contrib.contenttypes.models import ContentType
from services.controller.controller import service_controller


class ServiceRequestForm(forms.Form):
    """
    A Service request created by customer for a specific expert
    """

    service = forms.ModelChoiceField(queryset=Service.objects.all())

    class Meta:
        fields = ["service"]

    def save(self):
        request = ServiceRequest.objects.create(
            customer=self.customer,
            expert=self.expert,
            status=RequestStatus.WAIT_FOR_EXPERT_APPROVAL,
            request_type=RequestType.CUSTOMER_SELECTED,
            service=self.cleaned_data["service"],
        )
        return request

    def __init__(self, expert, customer, request=None, **kwargs):
        super(ServiceRequestForm, self).__init__(request, **kwargs)

        self.expert = expert
        self.customer = customer

        self.fields["service"].widget.attrs["placeholder"] = "انتخاب سرویس"
        self.fields["service"].label = "سرویس"
        self.fields["service"].help_text = None

        if expert:
            self.fields["service"].queryset = Service.objects.filter(
                pk=expert.role.expertise.id
            )

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
    """
    This form is used when the customer wants the system to recommend an expert
    """

    service = forms.ModelChoiceField(queryset=Service.objects.all())

    class Meta:
        fields = ["service"]

    def __init__(self, *args, **kwargs):
        super(ServiceRequestFromSystemForm, self).__init__(*args, **kwargs)
        self.fields["service"].label = "سرویس انتخاب شده"
        self.fields["service"].widget.attrs[
            "style"
        ] = "text-align: left; direction: ltr;"

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

    def save(self, customer):
        eligible_experts = service_controller.get_eligible_experts(
            self.cleaned_data["service"]
        )
        service_request = ServiceRequest(
            customer=customer,
            service=self.cleaned_data["service"],
            expert=None,
            status=RequestStatus.NO_EXPERT_FOUND,
            request_type=RequestType.SYSTEM_SELECTED,
        )
        for expert in eligible_experts:
            service_request = ServiceRequest(
                customer=customer,
                service=self.cleaned_data["service"],
                expert=expert,
                status=RequestStatus.WAIT_FOR_EXPERT_APPROVAL,
                request_type=RequestType.SYSTEM_SELECTED,
            )
            service_request.save()
            return service_request

        return service_request
