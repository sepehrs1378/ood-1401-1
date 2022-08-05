from django import forms

from messaging.models.ticket import Ticket
from messaging.models.ticket_message import TicketMessage


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["topic", "creator", "time_of_creation", "status"]

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields["creator"].widget.attrs["readonly"] = True
        self.fields["time_of_creation"].widget.attrs["readonly"] = True
        self.fields["status"].widget.attrs["readonly"] = True


class TicketMessageForm(forms.ModelForm):
    class Meta:
        model = TicketMessage
        fields = ["text", "file", "sender", "ticket", "time"]

    def __init__(self, *args, **kwargs):
        super(TicketMessageForm, self).__init__(*args, **kwargs)
        self.fields["sender"].widget.attrs["readonly"] = True
        self.fields["ticket"].widget.attrs["readonly"] = True
        self.fields["time"].widget.attrs["readonly"] = True
        self.fields["file"].required = False
