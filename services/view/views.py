from traceback import print_tb
from django.shortcuts import render, redirect
from users.models.customer import Customer
from users.models.expert import Expert

from services.models.service_request import RequestType
from services.view.forms import ServiceRequestForm, ServiceRequestFromSystemForm
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
        if request.method == "POST":
            form = ServiceRequestFromSystemForm(request.POST)
            if form.is_valid():
                service_request = form.save(request.user, self.controller)
                print(service_request)
                print(service_request.id)
                msg = "request sent"
                if service_request.expert is None:
                    return redirect("/users")
                else:
                    return redirect(
                        f"/services/request/finding?request_id={service_request.id}"
                    )
            msg = form.errors
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
        user_type = request.user.get_user_type_str()
        # filter based on user.role type
        experts = self.controller.get_all_experts()
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
                "all_services_tree": self.controller.get_service_category_trees(query)
            },
        )
