from django.db import models


class ServiceCategory(models.Model):
    """
    A service category
    They have tree like relationships (using 'parent' field)
    """

    name = models.CharField(blank=False, null=False, max_length=20)
    description = models.TextField()
    parent = models.ForeignKey(
        "ServiceCategory", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self) -> str:
        return (
            f"{self.name} --> {self.parent if self.parent is not None else self.type}"
        )
