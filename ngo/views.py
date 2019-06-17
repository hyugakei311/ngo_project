from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import User, Event
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .forms import UserLoginForm
from django.urls import reverse, reverse_lazy
from django.views import View

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
    # if this is a POST request we need to process the form data
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
                    #return render(request, UserManagementView, {'role': role})
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
    # return HttpResponse("You're logged out.")


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
        # return reverse('user_update', kwargs={'pk': self.object.pk})
        return reverse('listusers')

    # def get(self, request, *args, **kwargs):
    #     try:
    #         if self.request.session['role'] == 'admin':
    #             self.object = self.get_object()
    #             return super().get(request, *args, **kwargs)
    #     except KeyError:
    #         return HttpResponseRedirect(reverse('login'))
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

    # def get(self, request, *args, **kwargs):
    #     try:
    #         if self.request.session['role'] == 'admin':
    #             self.object = self.get_object()
    #             context = self.get_context_data(object=self.object)
    #             return self.render_to_response(context)
    #     except KeyError:
    #         return HttpResponseRedirect(reverse('login'))

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
    success_url = '/even/'

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


# class EventCreate(CreateView):
#     model = Event
#     fields = "__all__"
#     template_name_suffix = '_create_form'
#
#     success_url = '/event/'
#
#     def get(self, request, *args, **kwargs):
#         try:
#             if request.session['role'] == 'admin':
#                 return super().get(request, *args, **kwargs)
#         except KeyError:
#             pass
#         return HttpResponseRedirect(reverse('login'))


class EventUpdate(UpdateView):
    model = Event
    fields = "__all__"
    template_name_suffix = '_update_form'



    def get_success_url(self):
        # return reverse('event_update', kwargs={'pk': self.object.pk})
        return reverse('even_list')


    # def get(self, request, *args, **kwargs):
    #     try:
    #         if self.request.session['role'] == 'admin':
    #             self.object = self.get_object()
    #             return super().get(request, *args, **kwargs)
    #     except KeyError:
    #         return HttpResponseRedirect(reverse('login'))
    def get(self, request, *args, **kwargs):
        try:
            if request.session['role'] == 'admin':
                return super().get(request, *args, **kwargs)
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))