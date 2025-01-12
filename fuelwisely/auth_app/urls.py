from django.urls import path
from .views import *


urlpatterns = [
     path('', register_user, name='register'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='Login'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('dashboard/', views.dashboard, name='dashboard'),  
    # path('profile/',views.user_profile, name='profile')
]
