from rest_framework import serializers
from .models import Blog

class blogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'date']