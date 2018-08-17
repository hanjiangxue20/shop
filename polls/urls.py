#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: 2038770992qq.com

from django.urls import path, include
from . import views

#<a href="{% url 'polls:detail' question.id %}"> Vote again?</a>  模板会用到应用名字
app_name='polls'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results', views.results, name='results'),
#     path('<int:question_id>/vote', views.vote, name='vote'),
# ]
# 使用通用视图，改良 URLconf
# 第二个和第三个匹配准则中，路径字符串中匹配模式的名称已经由 <question_id> 改为 <pk>
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
