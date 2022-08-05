from django.shortcuts import render, redirect

from feedback.controller.controller import FeedbackController
from feedback.view.forms import FeedbackForm


class FeedbackView:

    def __init__(self, controller: FeedbackController):
        self.controller = controller

    def test(self, request):
        msg = ""
        if request.method == "POST":
            form = FeedbackForm(
                request.POST,
                
            )
            if form.is_valid():
                request = form.save()
                msg = "request sent"
                return redirect("/users")
            msg = form.errors
        else:
            form = FeedbackForm()
        return render(
            request=request,
            template_name="feedback/feedback.html",
            context={"request_form": form, "msg": msg},
        )
