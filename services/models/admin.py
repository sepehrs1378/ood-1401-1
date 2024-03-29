from django.contrib import admin

from services.models.service_request_limit import ServiceRequestLimit
from .service import Service
from .service_category import ServiceCategory
from .service_request import ServiceRequest


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "number_of_requests",
    )

    def number_of_requests(self, obj):
        return obj.requests.count()


class ServiceCategoryAdmin(admin.ModelAdmin):
    pass


class ServiceRequestAdmin(admin.ModelAdmin):
    pass


class ServiceRequestLimitAdmin(admin.ModelAdmin):
    pass


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(ServiceRequestLimit, ServiceRequestLimitAdmin)
