from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer

from rest_framework import viewsets


class RestaurantModelViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.select_related().all()
    serializer_class = RestaurantSerializer
    http_method_names = ['get']
