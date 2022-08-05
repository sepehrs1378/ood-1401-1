from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

from messaging.view.forms import TicketForm, TicketMessageForm
from messaging.controller.controller import MessagingController
from messaging.models.ticket import Ticket, TicketStatus
from messaging.models.ticket_message import TicketMessage

class MessagingView:
    def __init__(self, controller: MessagingController) -> None:
        self.controller = controller

    def create_ticket(self, request):
        msg = ""
        if request.method == "POST":
            form = TicketForm(
                request.POST,
                initial={
                    "creator": request.user.id,
                    "time_of_creation": datetime.now(),
                    "status": TicketStatus.CREATED,
                },
            )
            if form.is_valid():
                request = form.save()
                msg = "request sent"
                return redirect("/users")
            msg = form.errors
        form = TicketForm(
            initial={
                "creator": request.user.id,
                "time_of_creation": datetime.now(),
                "status": TicketStatus.CREATED,
            },
        )
        return render(
            request=request,
            template_name="messaging/create_ticket.html",
            context={"request_form": form, "msg": msg},
        )

    def show_ticket(self, request, ticket_id):
        ticket = Ticket.objects.filter(pk=ticket_id).first()
        try:
            messages = list(TicketMessage.objects.filter(ticket=ticket))
        except Exception as e:
            messages = []

        return render(
            request=request,
            template_name="messaging/show_ticket.html",
            context={"ticket": ticket, "ticket_messages": messages},
        )

    def send_ticket(self, request, ticket_id):
        msg = ""
        if request.method == "POST":
            form = TicketMessageForm(
                request.POST,
                request.FILES,
                initial={
                    "sender": request.user.id,
                    "ticket": ticket_id,
                    "time": datetime.now(),
                },
            )
            if form.is_valid():
                request = form.save()
                msg = "request sent"
                return redirect("/messaging/ticket/show/" + str(ticket_id))
            msg = form.errors
        form = TicketMessageForm(
            initial={
                "sender": request.user.id,
                "ticket": ticket_id,
                "time": datetime.now(),
            },
        )
        return render(
            request=request,
            template_name="messaging/send_ticket.html",
            context={"request_form": form, "msg": msg},
        )

    def send_message(self, request, channel_id):
        result = self.controller.send_message(
            request.user, channel_id, request.POST["text"]
        )

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
        channels = self.controller.get_channels_of_user(request.user)

        return render(
            request=request,
            template_name="messaging/chatroom.html",
            context={"channels": channels},
        )
