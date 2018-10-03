from rest_framework import serializers
from .models import Carts

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = '__all__'
