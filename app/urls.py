from django.urls import path
from .views import signup_view, home_view, login_view, logout_view, dashboard_view, profile_view, change_password_view, forgot_password_view

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home'),  
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('change-password/', change_password_view, name='change_password'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),  # Add this line
]

