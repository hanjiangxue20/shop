"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from df_user import views as user_view
from django.conf import settings

app_name = 'shop'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_view.login, name='login'),
    path('tinymce/', include('tinymce.urls')),
    path('user/', include('df_user.urls'), name='user'),  # name :为你的 URL 取名能使你在 Django 的任意地方唯一地引用它
    path('goods/', include('df_goods.urls')),
    path('polls/', include('polls.urls')),  # 投票
    path('blog/', include('blog.urls')),  # blog
    # path('accounts/',include('users.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__/',include(debug_toolbar.urls)))