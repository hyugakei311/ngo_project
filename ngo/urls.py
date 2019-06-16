from django.urls import path,  reverse_lazy
from .views import UserCreate, login, logout, UserManagementView, UserUpdate, UserDelete, Home, EventManagementView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('adduser', UserCreate.as_view(), name='user_create'),
    # path('login', auth_views.LoginView.as_view(), name='login'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('list-users/', UserManagementView.as_view(), name='listusers'),
    # path('list-users/', AdminNgoMang.userManagemen, name='listusers'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDelete.as_view(), name='user_delete'),
    path('event/', EventManagementView.as_view(), name='even_list'),
]
