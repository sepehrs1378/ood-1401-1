from typing import Dict, Type
from django.shortcuts import render, redirect
from users.controller.controller import UserController

from users.models.customer import Customer
from users.models.expert import Expert
from users.models.role import Role

from users.view.forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate


class UserView:
    """
    Provides views to be used by UI from User subsystem
    """

    forms: Dict = {
        Expert: ExpertRegisterForm,
        Customer: CustomerRegisterForm,
    }

    edit_forms: Dict = {
        Expert: ExpertEditProfileForm,
        Customer: CustomerEditProfileForm,
    }

    def __init__(self, controller: UserController):
        self.controller = controller

    def register_decorator(self, role_type: Type[Role]):
        def register_view(request):
            msg = ""
            if request.method == "POST":
                form = self.forms.get(role_type)(request.POST, request.FILES)
                if form.is_valid():
                    user = form.save()
                    login(request, user)
                    messages.success(request, "Registration successful.")
                    return redirect("/")
                messages.error(
                    request, "Unsuccessful registration. Invalid information."
                )
                msg = form.errors
            else:
                form = self.forms.get(role_type)()
            return render(
                request=request,
                template_name="users/register.html",
                context={
                    "register_form": form,
                    "msg": msg,
                    "user_type": role_type.__name__,
                },
            )

        return register_view

    def home_page(self, request):
        user_type = None
        service_requests = None
        if request.user and request.user.is_authenticated:
            user_type = request.user.get_user_type_str()
            service_requests = self.controller.get_service_requests_list(request.user)
        return render(
            request=request,
            template_name="index.html",
            context={
                "user_type": user_type,
                "service_requests": service_requests,
            }
            if user_type
            else {},
        )

    def login_request(self, request):
        msg = ""
        if request.method == "POST":
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("/users")
                else:
                    msg = "invalid user or pass"
                    messages.error(request, "Invalid username or password.")
            else:
                msg = form.errors
                messages.error(request, "Invalid username or password.")
        else:
            form = LoginForm()
        return render(
            request=request,
            template_name="users/login.html",
            context={"login_form": form, "msg": msg},
        )

    def change_expert_status(self, request):
        self.controller.change_expert_status(request.user)
        return redirect("/users")

    def render_profile_form(self, request, user: Type[User], role_type: Type[Role]):
        msg = ""
        if request.method == "POST":
            form = self.edit_forms.get(role_type)(user, request.POST, request.FILES)
            if form.is_valid():
                form.save(user)
                messages.success(request, "Edit Profile successful.")
                return redirect(request.path_info)
            messages.error(request, "Unsuccessful Edit Profile Invalid information.")
            msg = form.errors
        else:
            form = self.edit_forms.get(role_type)(user)
        return render(
            request=request,
            template_name="users/profile.html",
            context={
                "profile_form": form,
                "msg": msg,
                "user_type": request.user.get_user_type_str(),
                "profile_type": role_type.__name__
            },
        )

    def profile(self, role_type: Type[Role]):
        def profile_view(request):
            user = self.controller.get_user_info(request.user)
            return self.render_profile_form(request, user, role_type)
        return profile_view

    def edit_profile(self, request, user_id):
        user = self.controller.get_user(user_id)
        role_type = user.role.__class__
        return self.render_profile_form(request, user, role_type)

    def list_users(self, request):
        users = self.controller.get_all_users()
        return render(
            request=request,
            template_name="admin/users-list.html",
            context={
                "users": users,
            }
        )