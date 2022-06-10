from django.urls import path
from users.models.customer import Customer
from users.models.expert import Expert
from . import views

app_name = "users"

urlpatterns = [
    path(
        "register/customer",
        views.register_decorator(Customer),
        name="register-customer",
    ),
    path("register/expert", views.register_decorator(Expert), name="register-expert"),
    path("login", views.login_request, name="login"),
    path("", views.home_page, name="home"),
]
