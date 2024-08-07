from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from cars.serializers import AutoSerializer
from cars.filters import PriceRangeFilter
from cars.models import Auto


class AutoViewSet(ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [DjangoFilterBackend, PriceRangeFilter]
    filterset_fields = ["model", "fuel", "transmission", "name", "year",  "mileage", "price"]

    def retrieve(self, request, pk=None):
        queryset = Auto.objects.all()
        car = get_object_or_404(queryset, pk=pk)
        serializer = AutoSerializer(car)
        return Response(serializer.data)
