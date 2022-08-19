from typing import Dict, List, Union
from django.core.exceptions import *

from messaging.models import Channel, Message
from messaging.models import TicketChannel, TicketMessage
from users.models.user import User


class MessagingController:
    def create_ticket(self, user: User, title: str, text: str) -> None:
        ticket_channel = TicketChannel.objects.create(creator=user, title=title)
        TicketMessage.objects.create(ticket=ticket_channel, text=text, sender=user)

    def get_ticket_channels(self, user: User) -> List[TicketChannel]:
        user_type = user.get_user_type_str()
        if user_type == "customer" or user_type == "expert":
            ticket_channels = TicketChannel.objects.filter(creator_id=user.id).all()
        else:
            ticket_channels = TicketChannel.objects.all()

        for channel in ticket_channels:
            channel.contact_name = channel.get_contact_name(user)
            channel.header = channel.title

        return ticket_channels

    def send_ticket_message(self, user: User, ticket_id: int, msg: str) -> bool:
        user_type = user.get_user_type_str()
        ticket_channel = TicketChannel.objects.get(pk=ticket_id)
        if user_type == "customer" or user_type == "expert":
            TicketMessage.objects.create(ticket=ticket_channel, sender=user, text=msg)
        else:
            admin_user = User.objects.get(username="admin")
            TicketMessage.objects.create(
                ticket=ticket_channel, sender=admin_user, text=msg
            )

        return True

    def get_ticket_messages(self, user: User, ticket_id: int):
        user_type = user.get_user_type_str()

        messages = TicketMessage.objects.filter(ticket_id=ticket_id).all()
        for msg in messages:
            if user_type == "customer" or user_type == "expert":
                msg.is_sent_by_me = msg.sender_id == user.id
            else:
                # sender = User.objects.get(pk=msg.sender_id)
                msg.is_sent_by_me = msg.sender.username == "admin"

        return messages

    def get_channels(self, user: User) -> List[Channel]:
        # A channel belongs to a user if he's either the expert or the customer in it.
        query = Channel.objects.filter(customer__id=user.id)
        query |= Channel.objects.filter(expert__id=user.id)
        channels = query.all()

        for channel in channels:
            channel.contact_name = channel.get_contact_name(user)
            channel.header = channel.contact_name

        return channels

    def get_messages_of_channel(self, user: User, channel_id: int) -> List[Message]:
        channel = self.__get_channel_of_user(user, channel_id)
        if channel is None:
            return False

        Message.objects.filter(channel__id=channel_id, sender__id=user.id).update(
            is_seen=True
        )
        messages = Message.objects.filter(channel__id=channel_id).all()
        for msg in messages:
            msg.is_sent_by_me = msg.sender_id == user.id

        return messages

    def send_message(self, user: User, channel_id: int, msg: str) -> bool:
        channel = self.__get_channel_of_user(user, channel_id)
        if channel is None:
            return False

        Message.objects.create(channel=channel, sender=user, text=msg)

        return True

    def __get_channel_of_user(self, user: User, channel_id: int) -> Channel:
        # A channel belongs to a user if he's either the expert or the customer in it.
        query = Channel.objects.filter(customer__id=user.id)
        query |= Channel.objects.filter(expert__id=user.id)

        try:
            channel = Channel.objects.get(pk=channel_id)
        except ObjectDoesNotExist:
            return None

        return channel
