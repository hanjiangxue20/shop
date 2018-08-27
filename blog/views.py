from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Blog, Author, Entry
from blog import tasks
from django.http import HttpResponse, JsonResponse
from time import sleep
import json


def BlogilView(request):
    # 耗时任务，发送邮件     耗时任务  会超过5s才可以返回
    # sendMail()
    tasks.myMail.delay()
    # 其他行为
    blog = Blog.objects.values('name')
    return HttpResponse(json.dumps(list(blog)), content_type='application/json')


def task_test(request):
    res = tasks.add.delay(4, 5)
    print("start running task")
    # tasks.myMail.delay()
    print("async task res", res.get())
    return HttpResponse('res %s' % res.get())


