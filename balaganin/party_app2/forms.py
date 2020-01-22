from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import EventList


class EventListImageForm(ModelForm):
    class Meta:
        model = EventList
        fields = ['image']


# class EventListCountryChoicesPrices(ModelForm):
#     class Meta:
#         model = EventList
#         fields = ['country', 'price']
