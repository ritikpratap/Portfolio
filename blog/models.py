from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50, default='Unknown')

    def __str__(self):
        return self.title