from django import forms
from .models import Emp

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['first_name','last_name','employee_id','city', 'media_file']