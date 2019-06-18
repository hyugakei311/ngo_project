from django.contrib import admin

from .models import User, Event, EventUser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'password', 'role']
admin.site.register(User, UserAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'location', 'start_date', 'end_date',
                    'registration', 'ticket_adult', 'ticket_child']
admin.site.register(Event, EventAdmin)

class EventUserAdmin(admin.ModelAdmin):
    list_display = ['user','event','ticket_adult_numbers','ticket_child_numbers']
admin.site.register(EventUser,EventUserAdmin)
