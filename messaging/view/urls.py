from django.urls import path
from .views import *

app_name = "messaging"
messaging_view = MessagingView()

urlpatterns = [
    path("ticket/create", messaging_view.create_ticket, name="create_ticket"),
    path("ticket/send/<int:ticket_id>", messaging_view.send_ticket, name="send_ticket"),
    path("ticket/show/<int:ticket_id>", messaging_view.show_ticket, name="show_ticket"),
]
