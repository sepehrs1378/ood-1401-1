from typing import Dict, List, Union
from services.models.request_reject_relation import RequestRejectionRelation
from services.models.service import Service
from services.models.service_category import ServiceCategory
from services.models.service_request import RequestStatus, RequestType, ServiceRequest
from users.models.expert import Expert
from users.models.user import User
from django.contrib.contenttypes.models import ContentType


class ServiceController:
    def get_eligible_experts(self, service: Service) -> List[User]:
        eligible_experts = User.objects.filter(
            role__polymorphic_ctype=ContentType.objects.get_for_model(Expert),
        )
        return list(
            filter(
                lambda expert: expert.role.status
                and expert.role.expertise.id == service.id,
                eligible_experts,
            )
        )

    def get_expert_by_role_id(self, role_id: int) -> User:
        try:
            role = Expert.objects.filter(pk=role_id).first()
            return User.objects.filter(role=role).first()
        except Exception as e:
            return None

    def get_service_category_trees(self, query=None) -> List[Dict]:
        root_services = ServiceCategory.objects.filter(parent=None)
        service_json = []
        for root in root_services:
            obj = {
                "name": root.name,
                "id": root.id,
                "desc": root.description,
                "children": [],
            }
            service_json.append(obj)
            self.append_children(obj["children"], root, query)

        return service_json

    def append_children(
        self, children_list: List, parent: Union[ServiceCategory, Service], query: str
    ) -> None:
        children = ServiceCategory.objects.filter(parent=parent)

        if len(children) == 0:
            services = Service.objects.filter(category=parent)
            for service in services:
                if query is None or (
                    query in service.name or query in service.description
                ):
                    children_list.append(
                        {
                            "name": service.name,
                            "id": service.id,
                            "desc": service.description,
                        }
                    )
        else:
            for child in children:
                obj = {
                    "name": child.name,
                    "id": child.id,
                    "desc": child.description,
                    "children": [],
                }
                children_list.append(obj)
                self.append_children(obj["children"], child, query)

    def get_request_by_id(self, request_id: int) -> Union[ServiceRequest, None]:
        try:
            return ServiceRequest.objects.filter(pk=int(request_id)).first()
        except Exception as e:
            return None

    def get_request_by_id_and_expert(
        self, request_id: int, expert: User
    ) -> Union[ServiceRequest, None]:
        try:
            return ServiceRequest.objects.filter(pk=request_id, expert=expert).first()
        except Exception as e:
            return None

    def reject_request(self, req: ServiceRequest, expert: User) -> None:
        # Default is no expert found
        req.status = RequestStatus.NO_EXPERT_FOUND

        # Record rejection
        RequestRejectionRelation.objects.create(expert=expert, request=req)

        if req.request_type == RequestType.SYSTEM_SELECTED:
            # All eligible experts
            eligible_experts = self.get_eligible_experts(req.service)
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

    def accept_expert(self, request_id: int, customer: User) -> None:
        req = ServiceRequest.objects.filter(
            pk=request_id,
            customer=customer,
        ).first()
        req.status = RequestStatus.IN_PROGRESS
        req.save()

    def finish_request(self, request_id: int, expert: User) -> None:
        req = ServiceRequest.objects.filter(pk=request_id, expert=expert).first()
        req.status = RequestStatus.FINISHED
        req.save()

    def get_all_experts(self) -> List[User]:
        return list(
            User.objects.filter(
                role__polymorphic_ctype=ContentType.objects.get_for_model(Expert)
            )
        )

    def approve_request(self, request_id: int, expert: User) -> None:
        req = self.get_request_by_id_and_expert(request_id, expert)
        if req.request_type == RequestType.SYSTEM_SELECTED:
            req.status = RequestStatus.EXPERT_FOUND
        else:
            req.status = RequestStatus.IN_PROGRESS
        req.save()
