from django.urls import path,include
from . import views as df_user_view

urlpatterns = [
    path('register/',df_user_view.register),
    path('register_handle/',df_user_view.register_handle),
    path('login/',df_user_view.login),
    path('register_exist/',df_user_view.register_exist),
    path('login/',df_user_view.login),

]