from django.urls import path
from nlp_app.views import nlp

urlpatterns = [
    path('nlp/', nlp, name='nlp'),
]