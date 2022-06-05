from django.contrib import admin
from .user import User
from .customer import Customer
from .expert import Expert
from .it_manager import ITManager
from .manager import Manager


class UserAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


class ExpertAdmin(admin.ModelAdmin):
    pass


class ITManagerAdmin(admin.ModelAdmin):
    pass


class ManagerAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(ITManager, ITManagerAdmin)
admin.site.register(Expert, ExpertAdmin)
admin.site.register(Customer, CustomerAdmin)
