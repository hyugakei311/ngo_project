from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User, Event
from django.http import HttpResponseRedirect
from .forms import UserLoginForm
# Create your views here.


class UserCreate(CreateView):
    model = User
    fields = "__all__"
    success_url = '/login/'





def get_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserLoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserLoginForm()

    return render(request, 'ngo/login.html', {'form': form})