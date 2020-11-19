from django.contrib import admin
from .models import Customer, Airlines, Flights, Location, Hotel
# Register your models here.

admin.site.register(Customer)
admin.site.register(Airlines)
admin.site.register(Flights)
admin.site.register(Location)
admin.site.register(Hotel)

