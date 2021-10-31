from restaurants.models import Restaurant
from .address import AddressSerializer
from .payment_methods import PaymentMethodsSerializer
from .schedule import ScheduleSerializer

from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    paymentmethods = PaymentMethodsSerializer()
    schedule = ScheduleSerializer()

    class Meta:
        model = Restaurant
        fields = (
            'title', 'image', 'rating', 'address', 'paymentmethods', 'schedule'
        )
