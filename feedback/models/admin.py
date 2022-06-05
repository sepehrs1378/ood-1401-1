from django.contrib import admin
from .evaluation_feedback import EvaluationFeedback
from .evaluation_metric import EvaluationMetric
from .feedback import Feedback


class EvaluationFeedbackAdmin(admin.ModelAdmin):
    pass


class EvaluationMetricAdmin(admin.ModelAdmin):
    pass


class FeedbackAdmin(admin.ModelAdmin):
    pass


admin.site.register(EvaluationFeedback, EvaluationFeedbackAdmin)
admin.site.register(EvaluationMetric, EvaluationMetricAdmin)
admin.site.register(Feedback, FeedbackAdmin)
