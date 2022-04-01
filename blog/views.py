from django.shortcuts import render
from .models import Blog
from rest_framework import generics, filters
from .serializers import blogPostSerializer

# Create your views here.

class Blog_API_search(generics.ListCreateAPIView):
    search_fields = ['author']
    filter_backends = (filters.SearchFilter,)
    queryset = Blog.objects.all()
    serializer_class = blogPostSerializer