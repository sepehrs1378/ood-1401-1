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
    path("list", user_view.list_users, name="users_list"),
    path("profile/customer", user_view.profile(Customer), name="my_profile"),
    path("profile/expert", user_view.profile(Expert), name="my_profile"),
    path("profile/<int:user_id>", user_view.edit_profile, name="profile"),
    path("profile/delete/<int:user_id>", user_view.delete_profile, name="profile"),

]
