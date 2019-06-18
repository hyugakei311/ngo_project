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
        exclude = ('user','event','created_at','updated_at')

        # fields = {'user','event','ticket_adult_numbers', 'ticket_child_numbers'}
        # widgets = {'user': forms.HiddenInput(),
        #            'event': forms.HiddenInput(),
        #            'created_at':forms.HiddenInput(),
        #            'updated_at':forms.HiddenInput()}

