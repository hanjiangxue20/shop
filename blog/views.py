from django.shortcuts import render, redirect
from .models import Blog, Author, Entry
from .tasks import sendMail
from django.http import HttpResponse, JsonResponse
from time import sleep
import json

def BlogilView(request):
    # 耗时任务，发送邮件     耗时任务  会超过5s才可以返回
    # sendMail()
    sendMail.delay()
    # 其他行为
    blog = Blog.objects.values('name')
    return HttpResponse(json.dumps(list(blog)), content_type='application/json')
