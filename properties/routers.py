from rest_framework_nested import routers

from properties.views import RetailsViewSet, PropertyByDistanceAndCoordinatesViewSet

core_router = routers.SimpleRouter()
core_router.register(r'retails', RetailsViewSet, basename='retails')
core_router.register(r'property-by-distance-and-coordinates', PropertyByDistanceAndCoordinatesViewSet, basename='properties-by-distance-and-coordinates')

