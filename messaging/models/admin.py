from django.contrib import admin
from .ticket import Ticket, TicketMessage


class TicketAdmin(admin.ModelAdmin):
    pass


class TicketMesssageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketMessage, TicketMesssageAdmin)
