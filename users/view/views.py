from django.shortcuts import render, redirect

from users.models.customer import Customer
from users.models.expert import Expert
from .forms import CustomerRegisterForm, ExpertRegisterForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate


class UserCatalogue:
    """
    Provides views to be used by UI from User subsystem
    """

    forms = {Expert: ExpertRegisterForm, Customer: CustomerRegisterForm}

    def register_decorator(self, role_type):
        def request_register(request):
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

        return request_register

    def home_page(self, request):
        user_type = None
        if request.user and request.user.is_authenticated:
            user_type = request.user.get_user_type_str()

        return render(
            request=request,
            template_name="index.html",
            context={"user_type": user_type} if user_type else {},
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
        if (
            request.user
            and request.user.is_authenticated
            and isinstance(request.user.role, Expert)
        ):
            user_role = request.user.role
            user_role.status = not user_role.status
            user_role.save()

        return redirect("/users")
