from django.shortcuts import render, redirect
from messaging.models.ticket import Ticket
from services.models.service_request import ServiceRequest

from users.models.customer import Customer
from users.models.expert import Expert
from .forms import CustomerRegisterForm, ExpertRegisterForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages
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
        else:
            form = forms.get(user_type)()
        return render(
            request=request,
            template_name="users/register.html",
            context={
                "register_form": form,
                "msg": msg,
                "user_type": user_type.__name__,
            },
        )

    return request_register


def get_child_user(user_id):
    customer = None
    expert = None
    try:
        customer = Customer.objects.get(pk=user_id)
    except Exception as e:
        pass

    try:
        expert = Expert.objects.get(pk=user_id)
    except Exception as e:
        pass

    return customer if customer else expert


def get_related_requests(user):
    user = get_child_user(user)
    if user is None:
        return []
    elif isinstance(user, Customer):
        return list(ServiceRequest.objects.filter(customer=user))
    else:
        return list(ServiceRequest.objects.filter(expert=user))


def get_related_tickets(user):
    try:
        return list(Ticket.objects.filter(creator=user))
    except Exception as e:
        return []


def home_page(request):
    customer = None
    expert = None
    requests = []
    if request.user and request.user.is_authenticated:
        try:
            customer = Customer.objects.get(pk=request.user.id)
        except Exception as e:
            pass

        try:
            expert = Expert.objects.get(pk=request.user.id)
        except Exception as e:
            pass

        requests = get_related_requests(request.user.id)
        tickets = get_related_tickets(request.user)

    return render(
        request=request,
        template_name="index.html",
        context={
            "user_type": "expert" if expert else "customer",
            "requests": requests,
            "tickets": tickets,
        }
        if customer or expert
        else {},
    )


def login_request(request):
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
