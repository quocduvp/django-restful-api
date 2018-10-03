from rest_framework import serializers
from .models import motorbike


class MotorbikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = motorbike
