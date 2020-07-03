from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('filter/<int:topic_id>/',filter_view,name='filter'),
    path('post_question/',post_question,name='post_question'),
    path('add_answer/<int:que_id>',add_answer,name='add_answer'),
]
