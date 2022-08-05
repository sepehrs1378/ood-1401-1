from django.contrib import admin
from .ticket import Ticket
from .ticket_message import TicketMessage
from .channel import Channel
from .message import Message


class TicketAdmin(admin.ModelAdmin):
    pass


class TicketMesssageAdmin(admin.ModelAdmin):
    pass


class ChannelAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketMessage, TicketMesssageAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Message, MessageAdmin)
