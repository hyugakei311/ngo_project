from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User, Event
# Create your views here.


class UserCreate(CreateView):
    model = User
    fields = "__all__"
    success_url = '/login/'