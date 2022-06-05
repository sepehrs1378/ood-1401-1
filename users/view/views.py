from django.shortcuts import render, redirect

from users.models.customer import Customer
from users.models.expert import Expert
from .forms import CustomerRegisterForm, ExpertRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


forms = {Expert: ExpertRegisterForm, Customer: CustomerRegisterForm}


def register_decorator(user_type):
    def request_register(request):
        msg = ""
        if request.method == "POST":
            form = forms.get(user_type)(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect("/")
            messages.error(request, "Unsuccessful registration. Invalid information.")
            msg = form.errors
        form = forms.get(user_type)()
        return render(
            request=request,
            template_name="users/register.html",
            context={"register_form": form, "msg": msg},
        )

    return request_register


def home_page(request):
    return render(request=request, template_name="index.html")


def login_request(request):
    msg = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
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
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="users/login.html",
        context={"login_form": form, "msg": msg},
    )
