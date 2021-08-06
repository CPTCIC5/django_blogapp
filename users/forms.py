from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']


class UserUpdateForm(forms.ModelForm):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['first_name','last_name','username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields= ['image']