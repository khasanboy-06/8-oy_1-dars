from rest_framework import serializers
from .models import CarsInfo


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsInfo
        fields = ['id', 'name', 'year', 'content']