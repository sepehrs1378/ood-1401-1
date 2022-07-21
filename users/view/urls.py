from django.urls import path
from users.models.customer import Customer
from users.models.expert import Expert
from home_service.dependency_injection import dependency_injector

app_name = "users"
user_view = dependency_injector.user_view

urlpatterns = [
    path(
        "register/customer",
        user_view.register_decorator(Customer),
        name="register-customer",
    ),
    path(
        "register/expert",
        user_view.register_decorator(Expert),
        name="register-expert",
    ),
    path(
        "expert/change-status",
        user_view.change_expert_status,
        name="change_status",
    ),
    path("login", user_view.login_request, name="login"),
    path("", user_view.home_page, name="home"),
]
