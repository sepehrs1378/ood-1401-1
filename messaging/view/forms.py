from django import forms


class TicketForm(forms.Form):
    title = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"placeholder": "تیتر"})
    )
    text = forms.CharField(
        max_length=500, widget=forms.TextInput(attrs={"placeholder": "متن"})
    )

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields["title"].label = ""
        self.fields["text"].label = ""
