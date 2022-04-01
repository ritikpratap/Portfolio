from django.urls import path
from .views import Blog_API_search

urlpatterns = [
    path('blog/',Blog_API_search.as_view(),name="blog"),
]