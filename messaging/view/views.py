from datetime import datetime
from django.shortcuts import render, redirect
from messaging.models import ticket
from messaging.models.ticket import Ticket, TicketMessage, TicketStatus

from messaging.view.forms import TicketForm, TicketMessageForm


class MessagingView:
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
