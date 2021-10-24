from .views import RestaurantModelViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('restaurants', RestaurantModelViewSet)

urlpatterns = router.urls
