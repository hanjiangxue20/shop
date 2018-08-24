#!/usr/bin/python3
#-*-coding:utf-8-*-
# Author: 2038770992qq.com

from django.urls import path,include
from blog import views



app_name='blog'

urlpatterns=[
    path('email/',views.sendMail,name='email'),
    path('view/',views.BlogilView,name='blog_view'),
]
