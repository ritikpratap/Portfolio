from django.urls import path
from .views import oxford

urlpatterns = [
    path('oxford/',oxford,name="oxford"),
]