from django.shortcuts import render, redirect
from .models import Blog, Author, Entry
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from .tasks import sum
from time import sleep
import json


def sendMail():
    msg = '<a href="http://www.baidu.com" target="_blank">点击激活账户</a>'
    send_mail('测试邮件',
              '',
              settings.EMAIL_FROM,
              ['2469257690@qq.com',],
              html_message=msg
              )
    sleep(5)
    print('send email success!')
    return True
    # return HttpResponse('激活邮件已经发送，请注意查收！')


def BlogilView(request):
    # 耗时任务，发送邮件     耗时任务  会超过5s才可以返回
    rec_email = ['2469257690@qq.com', ]
    sendMail()
    # 其他行为
    blog = Blog.objects.values('name')
    return HttpResponse(json.dumps(list(blog)), content_type='application/json')

