from django import forms
from users.models import User, role, user, Customer
from services.models.service_request import RequestStatus, RequestType, ServiceRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from services.models.service import Service, ServiceCategory
from services.view.exceptions import RepeatedRequestException
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType


class ServiceRequestForm(forms.Form):
    """
    A Service request created by customer for a specific expert
    """

    service = forms.ModelChoiceField(queryset=Service.objects.all())

    class Meta:
        fields = ["service"]

    def save(self):
        customer_previous_requests = ServiceRequest.objects.filter(
            customer=self.customer,
            service=self.cleaned_data["service"],
            status=RequestStatus.IN_PROGRESS,
        )

        if len(customer_previous_requests) > 0:
            raise RepeatedRequestException()

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

    def save(self, customer, service_controller):
        customer_previous_requests = ServiceRequest.objects.filter(
            customer=customer,
            service=self.cleaned_data["service"],
            status=RequestStatus.IN_PROGRESS,
        )

        if len(customer_previous_requests) > 0:
            raise RepeatedRequestException()

        eligible_experts = service_controller.get_eligible_experts(
            self.cleaned_data["service"]
        )
        if len(eligible_experts) > 0:
            service_request = ServiceRequest(
                customer=customer,
                service=self.cleaned_data["service"],
                expert=None,
                status=RequestStatus.WAIT_FOR_EXPERT_APPROVAL,
                request_type=RequestType.SYSTEM_SELECTED,
            )
        else:
            service_request = ServiceRequest(
                customer=customer,
                service=self.cleaned_data["service"],
                expert=None,
                status=RequestStatus.NO_EXPERT_FOUND,
                request_type=RequestType.SYSTEM_SELECTED,
            )

        service_request.save()
        return service_request


class ServiceRequestForCustomerForm(forms.Form):
    """
    This form is used when the customer wants the system to recommend an expert
    """

    service = forms.ModelChoiceField(queryset=Service.objects.all())
    customer = forms.ModelChoiceField(queryset=User.objects.filter(role__polymorphic_ctype=ContentType.objects.get_for_model(Customer))) #todo: filter only customers
    class Meta:
        fields = ["service" , "customer"]

    def __init__(self, *args, **kwargs):
        super(ServiceRequestForCustomerForm, self).__init__(*args, **kwargs)
        self.fields["service"].label = "سرویس انتخاب شده"
        self.fields["service"].widget.attrs[
            "style"
        ] = "text-align: left; direction: ltr;"
        self.fields["customer"].label = "مشتری"
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                "service",
                css_class="container complete-rtl px-0 mx-0",
            ),
            Div(
                "customer",
                css_class="container complete-rtl px-0 mx-0",
            ),
            Submit(
                "submit",
                "ارسال درخواست",
                css_class="btn btn-dark py-2 mt-2",
            ),
        )

    def save(self, service_controller):
        customer_previous_requests = ServiceRequest.objects.filter(
            customer=self.cleaned_data["customer"],
            service=self.cleaned_data["service"],
            status=RequestStatus.IN_PROGRESS,
        )

        if len(customer_previous_requests) > 0:
            raise RepeatedRequestException()

        eligible_experts = service_controller.get_eligible_experts(
            self.cleaned_data["service"]
        )
        if len(eligible_experts) > 0:
            service_request = ServiceRequest(
                customer=self.cleaned_data["customer"],
                service=self.cleaned_data["service"],
                expert=None,
                status=RequestStatus.WAIT_FOR_EXPERT_APPROVAL,
                request_type=RequestType.SYSTEM_SELECTED,
            )
        else:
            service_request = ServiceRequest(
                customer=self.cleaned_data["customer"],
                service=self.cleaned_data["service"],
                expert=None,
                status=RequestStatus.NO_EXPERT_FOUND,
                request_type=RequestType.SYSTEM_SELECTED,
            )

        service_request.save()
        return service_request

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'category']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__( *args, **kwargs)
        self.fields["name"].label = "نام"
        self.fields["description"].label = "توضیحات"
        self.fields["category"].label = "دسته بندی"

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div("name", css_class="col"),
            Div("description", css_class="col"),
            Div("category", css_class="col"),
            Submit(
                "ُSave",
                "ذخیره",
                css_class="btn btn-dark py-2 mt-2",
                style="width: 10%",
            ))


class CategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['name', 'description', 'parent']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__( *args, **kwargs)
        self.fields["name"].label = "نام"
        self.fields["description"].label = "توضیحات"
        self.fields["parent"].label = "دسته بندی مادر"

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div("name", css_class="col"),
            Div("description", css_class="col"),
            Div("parent", css_class="col"),
            Submit(
                "ُSave",
                "ذخیره",
                css_class="btn btn-dark py-2 mt-2",
                style="width: 10%",
            ))
