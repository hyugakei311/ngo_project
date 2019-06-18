from django.forms import ModelForm, PasswordInput, Textarea, DateField, TimeField
from .models import *
from django import forms

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        widgets = {'password': PasswordInput}
        fields = ('email', 'password')


class EventUserViewForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'image']


class EventRegisterForm(ModelForm):

    class Meta:
        model = EventUser
        fields = {'ticket_adult_numbers', 'ticket_child_numbers'}

