from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label="", widget=forms.TextInput(attrs={'style': 'border-radius: 7px;','placeholder': 'Username'}))
    password = forms.CharField(max_length=100,label="", widget=forms.PasswordInput(attrs={'style': 'border-radius: 7px;', 'placeholder': 'Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username,password=password)
            
            if not user:
                raise forms.ValidationError("Incorrect username or password")
            return super(LoginForm, self).clean()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
        
    def clean_email(self):

        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')