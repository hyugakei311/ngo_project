from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import *
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, EventUserViewForm, EventRegisterForm
from django.urls import reverse, reverse_lazy
import datetime

# Create your views here.


class UserCreate(CreateView):
    model = User
    fields = "__all__"
    success_url = '/list-users/'

    def get(self, request, *args, **kwargs):
        try:
            if request.session['role'] == 'admin':
                return super().get(request, *args, **kwargs)
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))


def login(request):
    if request.method == 'POST':
        try:
            del request.session['role']
            del request.session['info_user']
        except KeyError:
            pass
        form = UserLoginForm(request.POST)
        femail = form.data.get('email')
        print(femail)
        try:
            if User.objects.get(email=femail, password=form.data.get('password')):
                user = User.objects.get(email=form.data.get('email'))
                user_role = user.role
                print("user role id  ", user_role)
                if user_role == 'ADMIN':
                    print("user is admin", user_role)
                    request.session['role'] = 'admin'
                    role = request.session['role']
                    userinfo= user.first_name, user.last_name,  role
                    request.session.modified = True
                    request.session['info_user'] = userinfo

                    return HttpResponseRedirect(reverse('listusers'))
                else:
                    print("user is not admin")
                    request.session['role'] = 'user'
                    return render(request, 'ngo/user.html', {'user': user})
        except User.DoesNotExist:
            form = UserLoginForm()
            error_message = "Incorrect email address or password! Please try again!"
            return render(request, 'ngo/login.html', {'form': form, "error_message": error_message})

    else:
        form = UserLoginForm()

        return render(request, 'ngo/login.html', {'form': form})


def logout(request):
    try:
        del request.session['role']
        del request.session['info_user']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('listusers'))

class UserManagementView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        try:
            if request.session['role'] == 'admin':
                return super().get(request, *args, **kwargs)
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))


class UserUpdate(UpdateView):
    model = User
    fields = "__all__"
    template_name_suffix = '_update_form'


    def get_success_url(self):
        return reverse('listusers')

    def get(self, request, *args, **kwargs):
        try:
            if request.session['role'] == 'admin':
                return super().get(request, *args, **kwargs)
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('listusers')

    def get(self, request, *args, **kwargs):
        try:
            if request.session['role'] == 'admin':
                return super().get(request, *args, **kwargs)
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))



class Home(TemplateView):
    template_name = 'ngo/index.html'


class EventCreate(CreateView):
    model = Event
    fields = "__all__"
    success_url = '/event/'

    def get(self, request, *args, **kwargs):
        try:
            if request.session['role'] == 'admin':
                return super().get(request, *args, **kwargs)
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))


class EventManagementView(ListView):
    model = Event
    fields = "__all__"

    def get(self, request, *args, **kwargs):
        try:
            if request.session['role'] == 'admin':
                return super().get(request, *args, **kwargs)
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))

class EventUpdate(UpdateView):
    model = Event
    fields = "__all__"
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('event_list')

    def get(self, request, *args, **kwargs):
        try:
            if request.session['role'] == 'admin':
                return super().get(request, *args, **kwargs)
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))


class EventListUserView(ListView):
    model = EventUserViewForm
    fields = "__all__"
    template_name_suffix = '_list_user'

    def get(self, request, *args, **kwargs):
        try:
            if request.session['role'] == 'admin':
                return super().get(request, *args, **kwargs)
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))


def event_details(request,id):
    event = get_object_or_404(Event, id=id)
    request.session['event'] = id
    return render(request, 'ngo/event_detail.html',
                  {'event':event})


class EventRegisterView(CreateView):
    model = EventUser
    template_name = 'ngo/event_registration.html'
    form_class = EventRegisterForm
    success_url = "register_success"


    def form_valid(self, form):
        self.model = form.save(commit=False)
        self.model.user = get_object_or_404(User, id=self.request.user.id)
        self.model.event = get_object_or_404(Event, id=self.request.session['event'])
        self.model.save()
        # return HttpResponseRedirect(self.get_success_url())
        if self.request.method == "GET":
            super(EventRegisterView, self).form_valid(form)
            return render(self.request, self.template_name, self.get_context_data(form=form))
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        ctx = super(EventRegisterView, self).get_context_data(**kwargs)
        ctx['event'] = get_object_or_404(Event, id=self.request.session['event'])
        return ctx

    def get_initial(self, *args, **kwargs):
        initial = super(EventRegisterView, self).get_initial(**kwargs)
        initial['event'] = get_object_or_404(Event, id=self.request.session['event'])
        return initial

    def get_success_url(self):
        try:
            del self.request.session['event']
        except KeyError:
            pass
        return reverse('register_success')

def register_success(request):
    try:
        del request.session['event']
    except KeyError:
        pass
    return render(request, 'ngo/register_success.html', {})
