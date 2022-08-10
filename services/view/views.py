from traceback import print_tb
from django.shortcuts import render, redirect
from feedback.models.feedback import Feedback
from services.view.exceptions import RepeatedRequestException
from users.models.customer import Customer
from users.models.expert import Expert

from services.models.service_request import RequestStatus, RequestType, ServiceRequest
from services.view.forms import ServiceRequestForm, ServiceRequestFromSystemForm, ServiceForm
from services.controller.controller import ServiceController


class ServiceView:
    def __init__(self, controller: ServiceController):
        self.controller = controller

    # Expert is chosen by customer
    def request_service_from_expert(self, request, role_id: int):
        msg = ""
        expert = self.controller.get_expert_by_role_id(role_id)
        if request.method == "POST":
            form = ServiceRequestForm(
                request=request.POST,
                expert=expert,
                customer=request.user,
            )

            try:
                if form.is_valid():
                    request = form.save()
                    msg = "request sent"
                    return redirect("/users")
                msg = form.errors
            except RepeatedRequestException:
                msg = "یک درخواست از این نوع سرویس در حال انجام است."

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
        if request.method == "POST":
            form = ServiceRequestFromSystemForm(request.POST)
            if form.is_valid():
                try:
                    service_request = form.save(request.user, self.controller)
                    print(service_request)
                    print(service_request.id)
                    msg = "request sent"
                    if service_request.status == RequestStatus.NO_EXPERT_FOUND:
                        return redirect("/users")
                    else:
                        return redirect(
                            f"/services/request/finding?request_id={service_request.id}"
                        )
                except RepeatedRequestException:
                    msg = "یک درخواست از این نوع سرویس در حال انجام است."
        else:
            form = ServiceRequestFromSystemForm()
        return render(
            request=request,
            template_name="services/request-service.html",
            context={
                "request_form": form,
                "msg": msg,
                "request_type": RequestType.SYSTEM_SELECTED,
                "all_services_tree": self.controller.get_service_category_trees(),
            },
        )

    def finding_expert(self, request):
        request_id = request.GET["request_id"]
        service_request = None
        try:
            service_request = self.controller.get_request_by_id(int(request_id))
        except Exception as e:
            print(e)

        return render(
            request=request,
            template_name="services/finding-expert.html",
            context={"service_request": service_request},
        )

    def approve_request(self, request, request_id):
        if request.user and request.user.is_authenticated:
            try:
                if request.user is None or not isinstance(request.user.role, Expert):
                    raise Exception("invalid user")

                self.controller.approve_request(request_id, request.user)
                return redirect("/users")
            except Exception as e:
                print(e)
                return redirect("/users")
        else:
            return redirect("/users")

    def reject_request(self, request, request_id):
        if request.user and request.user.is_authenticated:
            try:
                if request.user is None or not isinstance(request.user.role, Expert):
                    raise Exception("invalid user")

                # Find request
                req = self.controller.get_request_by_id_and_expert(
                    request_id, request.user
                )

                self.controller.reject_request(req, request.user)

                return redirect("/users")
            except Exception as e:
                print(e)
                return redirect("/users")
        else:
            return redirect("/users")

    def accept_expert(self, request, request_id):
        """
        Accept expert by customer
        """
        if request.user and request.user.is_authenticated:
            try:
                if not isinstance(request.user.role, Customer):
                    raise Exception("invalid user")

                self.controller.accept_expert(int(request_id), request.user)
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

                self.controller.finish_request(request_id, request.user)
                return redirect("/users")
            except Exception as e:
                print(e)
                return redirect("/users")
        else:
            return redirect("/users")

    def experts_list(self, request):
        query = request.GET.get("q")
        user_type = request.user.get_user_type_str()
        # filter based on user.role type
        experts = self.controller.get_all_experts(query)
        for expert in experts:
            expert.rate = self.controller.get_average_rate(expert)
        experts.sort(key=lambda x: x.rate, reverse=True)
        return render(
            request=request,
            template_name="services/experts-list.html",
            context={
                "experts": experts,
                "user_type": user_type,
            },
        )

    def services_list(self, request):
        query = request.GET.get("q")
        return render(
            request=request,
            template_name="services/service-list.html",
            context={
                "user_type": request.user.get_user_type_str(),
                "all_services_tree": self.controller.get_service_category_trees(query)
            },
        )

    def categories_list(self, request):
        categories = self.controller.get_categories()
        return render(request=request, template_name="admin/category-list.html", context={
            "categories": categories,
        })

    def service(self, request, service_id):
        msg = ""
        service = self.controller.get_service(service_id)
        if request.method == "POST":
            form = ServiceForm(request.POST, instance=service)
            form.save()
            return redirect("/services/list")
        elif request.method == "delete":
            service.delete()
            return redirect("/services/list")
        else:
            form = ServiceForm(instance=service)
            return render(
                request=request,
                template_name="admin/service.html",
                context={"form": form, "msg": msg},
            )