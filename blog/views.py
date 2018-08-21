from django.shortcuts import render,redirect
from .models import Blog,Author,Entry
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse,JsonResponse


def sendMail(request):
    msg = '<a href="http://www.baidu.com" target="_blank">点击激活账户</a>'
    send_mail('测试邮件',
              '',
              settings.EMAIL_FROM,
              ['2469257690@qq.com',],
              html_message=msg
              )
    return HttpResponse('激活邮件已经发送，请注意查收！')



