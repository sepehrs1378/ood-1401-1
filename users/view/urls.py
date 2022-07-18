from django.urls import path
from users.models.customer import Customer
from users.models.expert import Expert
from . import views

app_name = "users"
user_catalogue = views.UserCatalogue()

urlpatterns = [
    path(
        "register/customer",
        user_catalogue.register_decorator(Customer),
        name="register-customer",
    ),
    path(
        "register/expert",
        user_catalogue.register_decorator(Expert),
        name="register-expert",
    ),
    path(
        "expert/change-status",
        user_catalogue.change_expert_status,
        name="change_status",
    ),
    path("login", user_catalogue.login_request, name="login"),
    path("", user_catalogue.home_page, name="home"),
]
