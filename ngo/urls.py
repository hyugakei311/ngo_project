from django.urls import path,  reverse_lazy
from .views import UserCreate, get_login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', UserCreate.as_view(), name='homepage'),
    # path('login', auth_views.LoginView.as_view(), name='login'),
    path('login', get_login, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
