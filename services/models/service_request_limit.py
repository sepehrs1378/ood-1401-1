from django.db import models


class ServiceRequestLimit(models.Model):
    min_average_rate = models.IntegerField()
    max_average_rate = models.IntegerField()
    max_active_request = models.IntegerField()

    def __str__(self) -> str:
        return f"[{self.min_average_rate}, {self.max_average_rate}] <-- {self.max_active_request}"
