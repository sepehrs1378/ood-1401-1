from cmath import exp
import re
from django.shortcuts import render, redirect
from services.models.service import Service
from users.models.customer import Customer
from users.models.expert import Expert
from services.models.service_request import RequestStatus, ServiceRequest

from services.models.service_request import RequestType
from users.models.user import User
from .forms import ServiceRequestForm, ServiceRequestFromSystemForm
from django.contrib.contenttypes.models import ContentType


class ServiceCatalogue:
    # Expert is chosen by customer
    def request_service_from_expert(self, request, expert_id):
        msg = ""
        expert_role = Expert.objects.filter(pk=expert_id).first()
        expert = User.objects.filter(role=expert_role).first() if expert_role else None
        if request.method == "POST":
            form = ServiceRequestForm(
                request=request.POST, expert=expert, customer=request.user
            )
            if form.is_valid():
                request = form.save()
                msg = "request sent"
                return redirect("/users")
            msg = form.errors
        else:
            form = ServiceRequestForm(expert=expert, customer=request.user)
            if not expert:
                msg = "Invalid expert selected"
        return render(
            request=request,
            template_name="services/request-service.html",
            context={
                "request_form": form,
                "msg": msg,
                "request_type": RequestType.CUSTOMER_SELECTED,
                "expert": expert,
            },
        )

    # Expert is chosen by system
    def request_service_from_system(self, request):
        msg = ""
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

    def finding_expert(self, request, service_request_id):
        service_request = ServiceRequest.objects.filter(
            pk=int(service_request_id)
        ).first()
        return render(
            request=request,
            template_name="services/finding-expert.html",
            context={
                "request_id": service_request_id,
                "service_request": service_request,
            },
        )

    def approve_request(self, request, request_id):
        if request.user and request.user.is_authenticated:
            try:
                if request.user is None or not isinstance(request.user.role, Expert):
                    raise Exception("invalid user")

                req = ServiceRequest.objects.filter(
                    pk=request_id, expert=request.user
                ).first()
                req.status = RequestStatus.IN_PROGRESS
                req.save()
                return redirect("/users")
            except Exception as e:
                print(e)
                return redirect("/users")
        else:
            return redirect("/users")

    def finish_request(self, request, request_id):
        if request.user and request.user.is_authenticated:
            try:
                if request.user is None or not isinstance(request.user.role, Expert):
                    raise Exception("invalid user")

                req = ServiceRequest.objects.filter(
                    pk=request_id, expert=request.user
                ).first()
                req.status = RequestStatus.FINISHED
                req.save()
                return redirect("/users")
            except Exception as e:
                print(e)
                return redirect("/users")
        else:
            return redirect("/users")

    def experts_list(self, request):
        user_type = request.user.get_user_type_str()
        # filter based on user.role type
        experts = list(
            User.objects.filter(
                role__polymorphic_ctype=ContentType.objects.get_for_model(Expert)
            )
        )
        return render(
            request=request,
            template_name="services/experts-list.html",
            context={
                "experts": experts,
                "user_type": user_type,
            },
        )
