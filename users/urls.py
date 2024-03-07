from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from users.views import *

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegisterUser.as_view(), name='signup'),
    path('profile/', ProfileUser.as_view(), name='profile'),
]
