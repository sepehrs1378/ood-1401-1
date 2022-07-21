from unicodedata import category
from django.shortcuts import render, redirect
from services.models.request_reject_relation import RequestRejectionRelation
from services.models.service import Service
from users.models.customer import Customer
from users.models.expert import Expert
from services.models.service_request import RequestStatus, ServiceRequest
from services.models.service_category import ServiceCategory

from services.models.service_request import RequestType
from users.models.user import User
from .forms import ServiceRequestForm, ServiceRequestFromSystemForm
from django.contrib.contenttypes.models import ContentType
from services.controller.controller import service_controller


class ServiceView:
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
        if request.method == "POST":
            form = ServiceRequestFromSystemForm(request.POST)
            if form.is_valid():
                service_request = form.save(request.user)
                msg = "request sent"
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
                "all_services_tree": self.get_tree_structure_categories(),
            },
        )

    def get_tree_structure_categories(self):
        root_services = ServiceCategory.objects.filter(parent=None)
        service_json = []
        for root in root_services:
            obj = {"name": root.name, "id": root.id, "children": []}
            service_json.append(obj)
            self.append_children(obj["children"], root)

        return service_json

    def append_children(self, children_list, parent):
        children = ServiceCategory.objects.filter(parent=parent)

        if len(children) == 0:
            services = Service.objects.filter(category=parent)
            for service in services:
                children_list.append(
                    {
                        "name": service.name,
                        "id": service.id,
                    }
                )
        else:
            for child in children:
                obj = {"name": child.name, "id": child.id, "children": []}
                children_list.append(obj)
                self.append_children(obj["children"], child)

    def finding_expert(self, request):
        request_id = request.GET["request_id"]
        service_request = None
        try:
            service_request = ServiceRequest.objects.filter(pk=int(request_id)).first()
        except Exception as e:
            raise e
            print("error: ", request_id)

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

                req = ServiceRequest.objects.filter(
                    pk=request_id, expert=request.user
                ).first()
                if req.request_type == RequestType.SYSTEM_SELECTED:
                    req.status = RequestStatus.EXPERT_FOUND
                else:
                    req.status = RequestStatus.IN_PROGRESS
                req.save()
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
                req = ServiceRequest.objects.filter(
                    pk=request_id, expert=request.user
                ).first()
                # Default is no expert found
                req.status = RequestStatus.NO_EXPERT_FOUND

                # Record rejection
                RequestRejectionRelation.objects.create(
                    expert=request.user, request=req
                )

                if req.request_type == RequestType.SYSTEM_SELECTED:
                    # All eligible experts
                    eligible_experts = service_controller.get_eligible_experts(
                        req.service
                    )
                    # Experts that rejected the request
                    rejected_experts = list(
                        map(
                            lambda rejection: rejection.expert,
                            list(RequestRejectionRelation.objects.filter(request=req)),
                        )
                    )

                    for expert in eligible_experts:
                        if expert not in rejected_experts:
                            req.expert = expert
                            req.status = RequestStatus.WAIT_FOR_EXPERT_APPROVAL
                            break
                else:
                    req.status = RequestStatus.REJECTED_BY_EXPERT

                req.save()
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

                req = ServiceRequest.objects.filter(
                    pk=request_id,
                    customer=request.user,
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
