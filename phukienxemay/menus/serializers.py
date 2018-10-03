from rest_framework import serializers
from .models import SubMenu, Menu


class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    sub_menu = SubMenuSerializer(read_only=True, many=True)
    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'sub_menu']
