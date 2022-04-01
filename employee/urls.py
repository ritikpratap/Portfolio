from django.urls import path
from .views import (create_view, index, detail_view, update_view, delete_view)

urlpatterns = [
    path('create/',create_view,name="create"),
    path('<int:id>/update/',update_view,name="update"),
    path('<int:id>/delete/',delete_view,name="delete"),
    path('index/',index,name="index"),
    path('user/<int:id>/',detail_view,name="details"),
]