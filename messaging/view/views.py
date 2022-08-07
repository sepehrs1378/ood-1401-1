from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

from messaging.view.forms import TicketForm
from messaging.controller.controller import MessagingController


class MessagingView:
    def __init__(self, controller: MessagingController) -> None:
        self.controller = controller

    def create_ticket(self, request):
        msg = ""
        if request.method == "POST":
            form = TicketForm(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                self.controller.create_ticket(
                    request.user, form_data["title"], form_data["text"]
                )
                msg = "request sent"
                return redirect("/users/")
            msg = form.errors
        elif request.method == "GET":
            form = TicketForm()

        return render(
            request=request,
            template_name="messaging/create_ticket.html",
            context={"request_form": form, "msg": msg},
        )

    def show_all_tickets(self, request):
        ticket_channels = self.controller.get_ticket_channels(request.user)
        user_type = request.user.get_user_type_str()

        return render(
            request=request,
            template_name="messaging/chatroom.html",
            context={
                "channels": ticket_channels,
                "user_type": user_type,
                "is_for_chat": False,
            },
        )

    @csrf_exempt
    def send_ticket_message(self, request, ticket_id):
        body = request.body.decode()
        body = {body.split(":")[0]: body.split(":")[1]}

        result = self.controller.send_ticket_message(
            request.user, ticket_id, body["text"]
        )

        return HttpResponse(result)

    # Returns messages of a ticket channel
    def get_ticket_messages(self, request, ticket_id):
        messages = self.controller.get_ticket_messages(request.user, ticket_id)
        messages = [msg.__dict__ for msg in messages]
        for i, msg in enumerate(messages):
            msg = {key: msg[key] for key in msg if not key.startswith("_")}
            msg["time"] = str(msg["time"])
            messages[i] = msg

        return HttpResponse(json.dumps(messages))

    @csrf_exempt
    def send_message(self, request, channel_id):
        body = request.body.decode()
        body = {body.split(":")[0]: body.split(":")[1]}

        result = self.controller.send_message(request.user, channel_id, body["text"])

        return HttpResponse(result)

    # Returns messages of a chennel
    def get_messages(self, request, channel_id):
        messages = self.controller.get_messages_of_channel(request.user, channel_id)
        messages = [msg.__dict__ for msg in messages]
        for i, msg in enumerate(messages):
            msg = {key: msg[key] for key in msg if not key.startswith("_")}
            msg["time"] = str(msg["time"])
            messages[i] = msg

        return HttpResponse(json.dumps(messages))

    def get_chatroom(self, request):
        channels = self.controller.get_channels(request.user)
        user_type = request.user.get_user_type_str()

        return render(
            request=request,
            template_name="messaging/chatroom.html",
            context={"channels": channels, "user_type": user_type, "is_for_chat": True},
        )
