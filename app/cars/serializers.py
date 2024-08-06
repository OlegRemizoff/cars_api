from rest_framework.serializers import ModelSerializer
from cars.models import Auto


class AutoSerializer(ModelSerializer):
    
    class Meta:
        model = Auto
        fields = "__all__"