from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts.views import signup

urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
