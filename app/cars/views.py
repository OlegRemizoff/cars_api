from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from cars.serializers import AutoSerializer
from cars.filters import PriceRangeFilter
from cars.models import Auto

# ?max_price=450000

class AutoViewSet(ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [DjangoFilterBackend, PriceRangeFilter]
    filterset_fields = ["model", "fuel", "transmission", "name", "year",  "mileage", "price"]





