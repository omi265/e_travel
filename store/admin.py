from django.contrib import admin
from .models import Customer, Airlines, Flights
# Register your models here.

admin.site.register(Customer)
admin.site.register(Airlines)
admin.site.register(Flights)

