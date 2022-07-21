from django.contrib import admin
from .service import Service
from .service_category import ServiceCategory
from .service_request import ServiceRequest
from .request_reject_relation import RequestRejectionRelation


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


class ServiceRejectionRelationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(RequestRejectionRelation, ServiceRejectionRelationAdmin)
