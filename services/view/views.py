import re
from django.shortcuts import render, redirect
from services.models.service import Service
from users.models.customer import Customer
from users.models.expert import Expert
from services.models.service_request import RequestStatus, ServiceRequest

from services.models.service_request import RequestType
from .forms import ServiceRequestForm, ServiceRequestFromSystemForm


def get_customer(user_id):
    return Customer.objects.get(pk=user_id)


def get_expert(user_id):
    return Expert.objects.get(pk=user_id)


# Expert is chosen by customer
def request_service_from_expert(request, expert_id):
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
        if form.is_valid():
            request = form.save()
            msg = "request sent"
            return redirect("/users")
        msg = form.errors
    else:
        form = ServiceRequestForm(
            initial={
                "customer": user.id,
                "request_type": RequestType.CUSTOMER_SELECTED,
                "expert": expert_id,
            },
        )
    return render(
        request=request,
        template_name="services/request-service.html",
        context={
            "request_form": form,
            "msg": msg,
            "request_type": RequestType.CUSTOMER_SELECTED,
        },
    )


# Expert is chosen by system
def request_service_from_system(request):
    msg = ""
    user = get_customer(request.user.id)
    service_id = request.GET.get("service_id", Service.objects.first().id)
    if request.method == "POST":
        form = ServiceRequestFromSystemForm(
            request.POST,
            initial={
                "service": service_id,
            },
        )
        if form.is_valid():
            service_request = form.save()
            msg = "request sent"
            return redirect(f"/services/request/finding/{str(service_request.id)}")
        msg = form.errors
    else:
        form = ServiceRequestFromSystemForm(
            initial={
                "service": service_id,
            },
        )
    return render(
        request=request,
        template_name="services/request-service.html",
        context={
            "request_form": form,
            "msg": msg,
            "request_type": RequestType.SYSTEM_SELECTED,
        },
    )


def finding_expert(request, service_request_id):
    service_request = ServiceRequest.objects.filter(pk=int(service_request_id)).first()
    return render(
        request=request,
        template_name="services/finding-expert.html",
        context={"request_id": service_request_id, "service_request": service_request},
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


def experts_list(request):
    user_type = request.user.get_user_type_str()
    return render(
        request=request,
        template_name="services/experts-list.html",
        context={
            "experts": [],
            "user_type": user_type,
        },
    )
