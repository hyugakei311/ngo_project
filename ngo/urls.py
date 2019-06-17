from django.urls import path,  reverse_lazy
from .views import UserCreate, login, logout, UserManagementView, UserUpdate, UserDelete, Home, EventManagementView, EventCreate, EventUpdate
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('adduser/', UserCreate.as_view(), name='user_create'),
    # path('login', auth_views.LoginView.as_view(), name='login'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('list-users/', UserManagementView.as_view(), name='listusers'),
    # path('list-users/', AdminNgoMang.userManagemen, name='listusers'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDelete.as_view(), name='user_delete'),
    path('event/', EventManagementView.as_view(), name='even_list'),
    path('event/add', EventCreate.as_view(), name='event_create'),
    path('event/edit/<int:pk>/', EventUpdate.as_view(), name='event_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += serve(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)