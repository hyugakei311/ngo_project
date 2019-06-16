from django.contrib import admin

from .models import User, Event, EventUser
# Register your models here.

from django.contrib.auth.admin import UserAdmin


admin.site.register(User)
admin.site.register(Event)
admin.site.register(EventUser)
