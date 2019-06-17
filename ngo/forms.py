from django.forms import ModelForm, PasswordInput, Textarea, DateField, TimeField
from .models import User, Event
from django import forms

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        widgets = {'password': PasswordInput}
        fields = ('email', 'password')


# class EventCreateForm(ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name', 'description', 'category', 'location', 'start_date', 'end_date', 'registration', 'image', 'ticket_adult', 'ticket_child']
#         # widgets = {'description': Textarea,
#         #            'start_date': DateField,
#         #            'end_date': DateField,
#         #            'start_time ': TimeField,
#         #            'end_time': TimeField


    # name = models.CharField(max_length=50)
    # description = models.CharField(max_length=200)
    # category = models.CharField(max_length=1,choices=C_CATEGORY, default=CONFERENCE)
    # location = models.CharField(max_length=50, null=True)
    # start_date = models.DateField()
    # end_date = models.DateField()
    # start_time = models.TimeField()
    # end_time = models.TimeField()
    # registration = models.BooleanField()
    # image = models.ImageField(upload_to='media')
    # ticket_adult = models.DecimalField(max_digits=10, decimal_places=2)
    # ticket_child = models.DecimalField(max_digits=10, decimal_places=2)

# class EventForm(ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name', 'description', 'category', 'location', 'start_date', 'end_date', 'registration', 'image',
#                   'ticket_adult', 'ticket_child']

