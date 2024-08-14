from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from cars.models import Auto


class AutoSerializer(ModelSerializer):
    model = serializers.ReadOnlyField(source='model.name')
    fuel = serializers.CharField(source='get_fuel_display')
    transmission = serializers.CharField(source='get_transmission_display')
    
    class Meta:
        model = Auto
        fields = ["id", "name", "model", "year", "model", "fuel", "transmission", "price"]
