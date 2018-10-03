from rest_framework import serializers
from .models import Producer
class ProducerSerialer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'
