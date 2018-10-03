from rest_framework import serializers
from .models import Orders, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = OrderItem

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(read_only=True, many=True)
    class Meta:
        fields = '__all__'
        model = Orders