import math
from typing import Dict, List, Union
from django.contrib.contenttypes.models import ContentType

from feedback.models.feedback import Feedback
from services.models.service import Service
from services.models.service_category import ServiceCategory
from services.models.service_request import RequestStatus, RequestType, ServiceRequest
from services.models.service_request_limit import ServiceRequestLimit
from users.models import user
from users.models.expert import Expert
from users.models.user import User
from messaging.models import Channel, Message


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

    def can_expert_accept_more(self, expert):
        active_requests = ServiceRequest.objects.filter(
            expert=expert, status=RequestStatus.IN_PROGRESS
        )
        rate = self.get_average_rate(expert)
        limit = ServiceRequestLimit.objects.filter(
            max_average_rate=max(math.ceil(rate), 1)
        ).first()
        return active_requests.count() < limit.max_active_request

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
        if req.request_type == RequestType.SYSTEM_SELECTED:
            req.status = RequestStatus.WAIT_FOR_EXPERT_APPROVAL
            req.expert = None
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

        self.__create_channel_for_request(customer, req.expert, req)

    def finish_request(self, request_id: int, expert: User) -> None:
        req = ServiceRequest.objects.filter(pk=request_id, expert=expert).first()
        req.status = RequestStatus.FINISHED
        req.save()

    def get_all_experts(self, query=None) -> List[User]:
        return (
            list(
                filter(
                    lambda user: query in user.username or query in user.name,
                    list(
                        User.objects.filter(
                            role__polymorphic_ctype=ContentType.objects.get_for_model(
                                Expert
                            ),
                        )
                    ),
                )
            )
            if query is not None
            else list(
                User.objects.filter(
                    role__polymorphic_ctype=ContentType.objects.get_for_model(Expert),
                )
            )
        )

    def get_average_rate(self, expert):
        try:
            service_requests = ServiceRequest.objects.filter(expert=expert)
            rate_sum = 0
            rate_count = 0
            for service in service_requests:
                feedback = Feedback.objects.filter(service_request=service).first()
                try:
                    for rate in feedback.feedbacks.all():
                        rate_sum = rate_sum + rate.rate
                        rate_count = rate_count + 1
                except Exception:
                    pass
            return round(rate_sum / rate_count, ndigits=2)
        except Exception as e:
            print(e)
            return 0

    def approve_request(self, request_id: int, expert: User) -> None:
        req = ServiceRequest.objects.filter(pk=request_id).first()
        req.expert = expert
        if req.request_type == RequestType.SYSTEM_SELECTED:
            req.status = RequestStatus.EXPERT_FOUND
        else:
            req.status = RequestStatus.IN_PROGRESS
            self.__create_channel_for_request(req.customer, expert, req)
        req.save()

    def __create_channel_for_request(
        self, customer: User, expert: User, request: ServiceRequest
    ):
        channel = Channel.objects.create(
            customer=customer, expert=expert, related_service_request=request
        )
        starting_msg_text = "این کانال برای گفت‌و‌گوی مشتری و متخصص به وجود آمده است"
        Message.objects.create(channel=channel, sender=customer, text=starting_msg_text)

    def get_categories(self):
        return ServiceCategory.objects.all()

    def get_service(self, service_id):
        return Service.objects.get(id=service_id)

    def get_category(self, category_id):
        return ServiceCategory.objects.get(id=category_id)
