from rest_framework import serializers
from .models import image, accessory, tag, require_for
from rest_framework import response, status

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = tag


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = image

# danh sach cac xe phu hop voi phu tung
class RequiredForSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = require_for

class AccessorySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    require_for = RequiredForSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = accessory