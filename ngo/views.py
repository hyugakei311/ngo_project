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



# class UserCreateLog(View):
#     @staticmethod
#     def get(self, request, *args, **kwargs):
#         try:
#             if request.session['role'] == 'admin':
#                 return UserCreate.as_view()
#         except KeyError:
#             pass
#         return Home.as_view()


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

    # def get(self, request, *args, **kwargs):
    #     try:
    #         if request.session['role'] == 'admin':
    #             self.object_list = self.get_queryset()
    #             allow_empty = self.get_allow_empty()
    #             if not allow_empty:
    #                 # When pagination is enabled and object_list is a queryset,
    #                 # it's better to do a cheap query than to load the unpaginated
    #                 # queryset in memory.
    #                 if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
    #                     is_empty = not self.object_list.exists()
    #                 else:
    #                     is_empty = not self.object_list
    #                 if is_empty:
    #                     raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.") % {
    #                         'class_name': self.__class__.__name__,
    #                     })
    #             context = self.get_context_data()
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


class UserUpdate(UpdateView):
    model = User
    fields = "__all__"
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('user_update', kwargs={'pk': self.object.pk})

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


# class UserView(DetailView):
#     model = User
#     template_name_suffix = '_detail'
#
#     def get(self, request, *args, **kwargs):
#         try:
#             if request.session['role'] == 'admin':
#                 self.object = self.get_object()
#                 context = self.get_context_data(object=self.object)
#                 return self.render_to_response(context)
#         except KeyError:
#             return HttpResponseRedirect(reverse('login'))


class EventCreate(CreateView):
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


class EventManagementView(ListView):
    model = Event

    def get(self, request, *args, **kwargs):
        try:
            if request.session['role'] == 'admin':
                return super().get(request, *args, **kwargs)
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))