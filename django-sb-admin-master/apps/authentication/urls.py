# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('user_list/', views.user_list, name='user_list'),
    path('file_list/', views.file_list, name='file_list'),
    path('count/', views.count, name='count'),
    path('runAction/<str:action>/<str:email>/', views.runAction, name='runAction'),
    

]
