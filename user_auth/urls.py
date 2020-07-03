from django.contrib import admin
from django.urls import path
from user_auth.views import *

urlpatterns = [
    #path('',index,name='index'),
    path('signup/',sign_up,name='signup'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('change_password/',change_password,name='change_password'),
]
