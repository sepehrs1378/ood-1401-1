from django import forms


class TicketForm(forms.Form):
    title = forms.CharField(max_length=30)
    text = forms.CharField(max_length=500)

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
