from users.models.expert import Expert
from users.models.user import User
from django.contrib.contenttypes.models import ContentType


class ServiceController:
    def get_eligible_experts(self, service):
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


service_controller = ServiceController()
