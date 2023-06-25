from rest_framework import serializers, fields
from .models import *

'''class ItemSerializer(serializers.ModelSerializer):

    quantities = QuantitySerializer(many=True)
    addons = AddonSerializer(many=True)
    category_name = serializers.CharField(source='category.name')
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Item
        fields = ('id', 'name', 'api_name', 'description', 'image_url', 'category_name', 'quantities', 'is_enabled', 'addons')

    def get_image_url(self, obj):
        if(obj.image):
            return obj.image.url
        return None'''