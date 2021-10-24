from .models import Address, PaymentMethods, Restaurant

from django.contrib import admin

# Register your models here.


class AddressInline(admin.TabularInline):
    model = Address


class PaymentMethodsInline(admin.TabularInline):
    model = PaymentMethods


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    inlines = [AddressInline, PaymentMethodsInline]
