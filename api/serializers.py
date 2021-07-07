from rest_framework import serializers
from cars.models import CarDetail

class CarDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model= CarDetail
        fields='__all__'