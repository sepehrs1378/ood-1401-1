from django.urls import path
from .views import *

app_name = "messaging"

urlpatterns = [
    path("ticket/create", create_ticket, name="create_ticket"),
    path("ticket/send/<int:ticket_id>", send_ticket, name="send_ticket"),
    path("ticket/show/<int:ticket_id>", show_ticket, name="show_ticket"),
]
