from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=15)
    country = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)


    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','phone','country','city']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email','first_name','last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country','phone','city','image']