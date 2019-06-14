from django.forms import ModelForm, PasswordInput
from .models import User

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        widgets = {'password': PasswordInput}
        fields = ('email', 'password')