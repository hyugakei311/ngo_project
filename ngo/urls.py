from django.urls import path,  reverse_lazy
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from .models import Event
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
    path('event/', EventManagementView.as_view(), name='event_list'),
    path('event/add', EventCreate.as_view(), name='event_create'),
    path('event/edit/<int:pk>/', EventUpdate.as_view(), name='event_update'),
    path('event/list/', EventListUserView.as_view(model = Event), name='event_user_list'),
    path('event/<int:id>', event_details, name='event_details'),
    path('event/<int:id>/register', EventRegisterView.as_view(), name="event_register"),
    path('event/register/success', register_success, name="register_success")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += serve(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)