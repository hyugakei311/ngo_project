from django.db import models

# Create your models here.


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
    role = models.CharField(max_length=1, choices=R_ROLE,  default=USER,)


class Event(models.Model):

    C_CATEGORY = (
        ('C', 'Conference'),
        ('S', 'Seminar'),
        ('P', 'Presentation'),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.DateField(max_length=1,choices=C_CATEGORY)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    registration = models.BooleanField()
    image = models.CharField(max_length=200)
    ticket_adult = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_child = models.DecimalField(max_digits=10, decimal_places=2)




