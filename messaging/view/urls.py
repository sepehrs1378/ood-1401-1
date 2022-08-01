from django.urls import path
from .views import *
from home_service.dependency_injection import dependency_injector

app_name = "messaging"
messaging_view = dependency_injector.messaging_view

urlpatterns = [
    path("ticket/create", messaging_view.create_ticket, name="create_ticket"),
    path("ticket/send/<int:ticket_id>", messaging_view.send_ticket, name="send_ticket"),
    path("ticket/show/<int:ticket_id>", messaging_view.show_ticket, name="show_ticket"),
    path(
        "chatroom/channel/<int:channel_id>/send/",
        messaging_view.send_message,
        name="send_message",
    ),
    path(
        "chatroom/channel/<int:channel_id>/get-messages/",
        messaging_view.get_messages,
        name="get_messages",
    ),
    path("chatroom/", messaging_view.get_chatroom, name="get_chatroom"),
]
