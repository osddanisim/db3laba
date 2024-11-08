from django.contrib import admin
from .models import User, Car, ServiceStation, Service, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone_number')
    search_fields = ('name', 'surname', 'email')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'year', 'license_plate', 'user')
    search_fields = ('model', 'brand', 'license_plate')
    list_filter = ('year',)

@admin.register(ServiceStation)
class ServiceStationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'address', 'contact_info')
    search_fields = ('station_name', 'address')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'price', 'station')
    search_fields = ('service_name',)
    list_filter = ('station',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'service', 'order_date', 'order_status')
    search_fields = ('order_status',)
    list_filter = ('order_date', 'order_status')
