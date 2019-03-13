from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',
        auth_views.LoginView.as_view(),
        name='Login'),
    path('logout/',
        auth_views.LogoutView.as_view(),
        name='Logout'),
    path('signup/', views.SignUp.as_view(), name="SignUp"),
]
