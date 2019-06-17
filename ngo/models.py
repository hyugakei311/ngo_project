from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class CustomDateTimeField(models.DateTimeField):
#     def value_to_string(self, obj):
#         val = self.value_from_object(obj)
#         if val:
#             val.replace(microsecond=0)
#             return val.isoformat()
#         return ''


class User(models.Model):
    USER = 'User'
    ADMIN = 'Admin'
    R_ROLE = (
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=5, choices=R_ROLE,  default=USER,)

    @property
    def is_authenticated(self, request):
        user_role = 'not_login'
        if request.session['role'] == 'admin':
            user_role = 'admin'
        elif request.session['role'] == 'user':
            user_role = 'user'
        return user_role


class Event(models.Model):
    CONFERENCE= 1
    SEMINAR= 2
    PRESENTATION = 3
    C_CATEGORY = (
        ('C', 'Conference'),
        ('S', 'Seminar'),
        ('P', 'Presentation'),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # user = models.ManyToManyField(User)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=1,choices=C_CATEGORY, default=CONFERENCE)
    location = models.CharField(max_length=50, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    registration = models.BooleanField()
    image = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, default='/static/ngo/images/no_image_available.jpg')
    ticket_adult = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_child = models.DecimalField(max_digits=10, decimal_places=2)


class EventUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)



