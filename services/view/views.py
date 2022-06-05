from django.shortcuts import render, redirect
from users.models.customer import Customer
from users.models.expert import Expert
from services.models.service_request import RequestStatus, ServiceRequest

from services.models.service_request import RequestType
from .forms import ServiceRequestForm


def get_customer(user_id):
    return Customer.objects.get(pk=user_id)


def get_expert(user_id):
    return Expert.objects.get(pk=user_id)


def request_service(request):
    msg = ""
    user = get_customer(request.user.id)
    if request.method == "POST":
        form = ServiceRequestForm(
            request.POST,
            initial={
                "customer": user.id,
                "request_type": RequestType.CUSTOMER_SELECTED,
            },
        )
        print("mohsen", form.fields["customer"])
        if form.is_valid():
            print("salam", "form is valid")
            request = form.save()
            msg = "request sent"
            return redirect("/users")
        msg = form.errors
    form = ServiceRequestForm(
        initial={"customer": user.id, "request_type": RequestType.CUSTOMER_SELECTED},
    )
    print(form.fields["customer"])
    return render(
        request=request,
        template_name="services/request_service.html",
        context={"request_form": form, "msg": msg},
    )


def approve_request(request, request_id):
    if request.user and request.user.is_authenticated:
        try:
            user = get_expert(request.user.id)
            if user is None:
                raise Exception("invalid user")

            req = ServiceRequest.objects.filter(pk=request_id, expert=user).first()
            req.status = RequestStatus.IN_PROGRESS
            req.save()
            return redirect("/users")
        except Exception as e:
            print(e)
            return redirect("/users")
    else:
        return redirect("/users")


def finish_request(request, request_id):
    if request.user and request.user.is_authenticated:
        try:
            user = get_expert(request.user.id)
            if user is None:
                raise Exception("invalid user")

            req = ServiceRequest.objects.filter(pk=request_id, expert=user).first()
            req.status = RequestStatus.FINISHED
            req.save()
            return redirect("/users")
        except Exception as e:
            print(e)
            return redirect("/users")
    else:
        return redirect("/users")
