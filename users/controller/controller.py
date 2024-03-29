from django.db.models import Q
from services.controller.controller import ServiceController
from users.models.user import User
from users.models.expert import Expert
from users.models.customer import Customer
from users.models.it_manager import ITManager
from users.models.manager import Manager
from services.models.service_request import ServiceRequest


class UserController:
    def get_service_requests_list(self, user: User):
        if isinstance(user.role, Customer):
            return ServiceRequest.objects.filter(customer=user)
        elif isinstance(user.role, Expert):
            service_controller = ServiceController()
            try:
                if service_controller.can_expert_accept_more(user):
                    return ServiceRequest.objects.filter(
                        Q(expert=user) | Q(expert=None, service=user.role.expertise)
                    )
                else:
                    return ServiceRequest.objects.filter(expert=user)
            except Exception as e:
                return ServiceRequest.objects.filter(
                    Q(expert=user) | Q(expert=None, service=user.role.expertise)
                )
        elif isinstance(user.role, ITManager):
            return ServiceRequest.objects.all()
        elif isinstance(user.role, Manager):
            return ServiceRequest.objects.all()
        return []

    def change_expert_status(self, user: User):
        if user and user.is_authenticated and isinstance(user.role, Expert):
            user_role = user.role
            user_role.status = not user_role.status
            user_role.save()

    def get_user_info(self, user: User):
        return User.objects.get(username=user.username)

    def get_user(self, user_id: int):
        return User.objects.get(id=user_id)

    def check_username_is_repetitive(myPk, myUsername):
        return User.objects.filter(~Q(pk=myPk) & Q(username=myUsername)).exists()

    def check_email_is_repetitive(myPk, myEmail):
        return User.objects.filter(~Q(pk=myPk) & Q(email=myEmail)).exists()

    def get_all_users(self):
        return User.objects.all()
