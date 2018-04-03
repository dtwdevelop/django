from django.contrib import admin
from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):

    readonly_fields = ['ip','geo_location']
    list_display = ('title','created')

# Register your models here.
admin.site.register(Delivery,DeliveryAdmin)
