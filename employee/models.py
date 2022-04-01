from django.db import models
from .validator import validate_file_size
from django.contrib.auth.models import User

# Create your models here.
class Emp(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id =  models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    media_file = models.FileField(upload_to ='uploads/', default="",  blank= False, validators=[validate_file_size])
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.first_name