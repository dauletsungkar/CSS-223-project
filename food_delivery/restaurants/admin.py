from .models import Address, PaymentMethods, Restaurant, Schedule

from django.contrib import admin

# Register your models here.


class AddressInline(admin.TabularInline):
    model = Address


class PaymentMethodsInline(admin.TabularInline):
    model = PaymentMethods


class ScheduleInline(admin.TabularInline):
    model = Schedule


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [AddressInline, PaymentMethodsInline, ScheduleInline]
    exclude = ('rating',)
