from django.core.exceptions import ValidationError
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
        return f"{self.name} <-- {self.parent}" if self.parent else f"{self.name}"

    class Meta:
        verbose_name = "ServiceCategory"
        verbose_name_plural = "ServiceCategories"

    def clean(self, *args, **kwargs):
        if self.parent and self.parent.id == self.id:
            raise ValidationError('دسته بندی مادر نمی‌تواند خودش باشد!')
        return super(ServiceCategory, self).clean(*args, **kwargs)