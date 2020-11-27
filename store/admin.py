from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer, Airlines, Flights, Location, Hotel, Ticket
# Register your models here.

admin.site.register(Customer)
admin.site.register(Airlines)
admin.site.register(Flights)
admin.site.register(Location)
admin.site.register(Hotel)
admin.site.register(Ticket)

"""
class ProfileInline(admin.StackedInline):
    model = Customer
    can_delete = False
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
"""