from typing import Dict, List, Union
from django.core.exceptions import *

from messaging.models import Channel, Message
from users.models.user import User


class MessagingController:
    def get_channels_of_user(self, user: User) -> List[Channel]:
        # A channel belongs to a user if he's either the expert or the customer in it.
        query = Channel.objects.filter(customer__id=user.id)
        query |= Channel.objects.filter(expert__id=user.id)

        channels = query.all()
        for channel in channels:
            channel.contact_name = channel.get_contact_name(user)

        return channels

    def get_messages_of_channel(self, user: User, channel_id: int) -> List[Message]:
        channel = self.__get_channel_of_user(user, channel_id)
        if channel is None:
            return False

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
