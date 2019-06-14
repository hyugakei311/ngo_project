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
        print("dddeeeeeeeeeeeeeeeeeeeeeeeeee")
        # create a form instance and populate it with data from the request:
        form = UserLoginForm(request.POST)

        # form.data.get("password")
        if User.objects.get(email=form.data.get('email'), password=form.data.get('password')):
            print('email')
        else:
            print('no email')

       # check whether it's valid:


        if form.is_valid():

            User.objects.get(email=1)
            print("ddddddddddddddddddddddddddddddddddd")
            print(form)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserLoginForm()

    return render(request, 'ngo/login.html', {'form': form})