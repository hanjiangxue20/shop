from django.shortcuts import render
from django.http import *
from .models import *
import hashlib

def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    #接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    #判断2次密码
    if upwd != upwd2:
        return HttpResponseRedirect('user/register/')
    #密码加密
    h1 = hashlib.md5()
    h1.update(upwd.encode(encoding='utf-8'))
    upwd3=h1.hexdigest()
    #合法 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    #注册成功，转到登录页
    return HttpResponseRedirect('/user/login/')

def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname ==uname).count()
    return JsonResponse({'count': count})

def login(request):
    return render(request,'df_user/login.html')