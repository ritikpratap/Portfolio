from rest_framework import serializers
from api_basic.models import Dishes

class DishPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = ['name', 'price', 'Restaurant']