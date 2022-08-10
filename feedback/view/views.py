from django.shortcuts import render, redirect

from feedback.view.forms import FeedbackForm, MetricForm
from feedback.models.evaluation_metric import EvaluationMetric
from django.contrib import messages

class FeedbackView:
    def send_feedback(self, request, request_id):
        msg = ""
        evaluation_metrics = EvaluationMetric.objects.all()
        if request.method == "POST":
            form = FeedbackForm(
                request=request.POST,
                metrics=evaluation_metrics,
                request_id=request_id,
                is_editable=True,
            )
            if form.is_valid():
                feedback = form.save()
                msg = "feedback saved"
                return redirect("/users")
            msg = form.errors
        else:
            form = FeedbackForm(
                metrics=evaluation_metrics,
                request_id=request_id,
                is_editable=True,
            )

        return render(
            request=request,
            template_name="feedback/send-feedback-page.html",
            context={
                "is_expert": False,
                "form": form,
                "msg": msg,
            },
        )

    def get_feedback(self, request, request_id):
        msg = ""
        evaluation_metrics = EvaluationMetric.objects.all()
        form = FeedbackForm(
            metrics=evaluation_metrics,
            request_id=request_id,
            is_editable=False,
        )
        form.initiate_from_feedback()

        return render(
            request=request,
            template_name="feedback/send-feedback-page.html",
            context={
                "is_expert": True,
                "form": form,
                "msg": msg,
            },
        )

    def metrics_list(self, request):
        evaluation_metrics = EvaluationMetric.objects.all()
        return render(
            request=request,
            template_name="admin/metrics-list.html",
            context={
                "metrics": evaluation_metrics,
            }
        )

    def metric(self, request, metric_id:int):
        msg=""
        metric = EvaluationMetric.objects.get(id=metric_id)
        if request.method == "POST":
            form = MetricForm(request.POST,instance=metric)
            if form.is_valid():
                form.save()
                messages.success(request, "Edit Metric successful.")
                return redirect("/feedback/metrics")
            messages.error(request, "Unsuccessful Edit Metric Invalid information.")
            msg = form.errors
        elif request.method == "delete":
            metric.delete()
            return redirect("/feedback/metrics")
        else:
            form = MetricForm(instance=metric)
        return render(
            request=request,
            template_name="admin/metric.html",
            context={"form": form, "msg": msg},
        )