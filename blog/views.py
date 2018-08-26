from django.shortcuts import render, redirect
from .models import Blog, Author, Entry
from blog import tasks
from django.http import HttpResponse, JsonResponse
from time import sleep
import json



def BlogilView(request):
    # 耗时任务，发送邮件     耗时任务  会超过5s才可以返回
    # sendMail()
    print((tasks.sendMail))
    tasks.sendMail.delay()
    # 其他行为
    data = list(Blog.objects.values('name'))
    return HttpResponse(json.dumps(data), content_type='application/json')
