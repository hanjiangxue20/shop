#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: 2038770992qq.com
from __future__ import absolute_import

import datetime
import time

from celery.schedules import crontab
from celery.task import periodic_task
from django.core.mail import send_mail
# from django_redis import cache
from shop import celery_app
from celery import shared_task
from celery.utils.log import get_task_logger
from time import sleep
from .models import *
from django.db.models import F
from django.conf import settings

logger = get_task_logger(__name__)


# app =Celery('tasks',broker='redis://127.0.0.1:6379/5',backend='redis://127.0.0.1:6379/5')
@celery_app.task()
def add(x, y):
    sleep(5)
    return x + y


@celery_app.task()
def add1(x, y):
    return x + y


@shared_task(ignore_result=True)
def log_result(result):
    logger.info('log_result got: %r', result)


@celery_app.task
def incr_readtime(article_id):
    return Article.objects.filter(id=article_id).update(score=F('score') + 1)


@celery_app.task
def create_blog(name, tagline):
    Blog.objects.create(name=name, tagline=tagline)


@celery_app.task()
def myMail():
    msg = '<a href="http://www.baidu.com" target="_blank">点击激活账户</a>'
    send_mail('测试邮件',
              '',
              settings.EMAIL_FROM,
              ['2469257690@qq.com', ],
              html_message=msg
              )
    # sleep(2)
    print('send email success!')
    return True


# @periodic_task(run_every=3)  #3秒   定时周期任务：每三秒
@periodic_task(run_every=datetime.timedelta(hours=0, minutes=0, seconds=3))  # 3秒   定时周期任务：每三秒
# @periodic_task(run_every=crontab(minute='55',hour=20)) #定时：20:55分
# @periodic_task(run_every=crontab(minute='*/2')) #没隔2分钟=crontab(minute='0-59/2')  这个/号不是除以的意思。相当与range的第3个参数
def some_task():
    print('periodic task test!')
    # sleep(5)
    print('success:{}'.format(time.ctime()))
    return True


@periodic_task(run_every=crontab(minute=9, hour=14, day_of_week='0-4', ))  # 工作日9点
def say_hello():
    print('Good morning!')
    msg = '<a href="http://www.baidu.com" target="_blank">点击激活账户</a>'
    send_mail('测试邮件',
              '',
              settings.EMAIL_FROM,
              ['2469257690@qq.com', ],
              html_message=msg
              )
    # sleep(2)
    print('send email success!')

@periodic_task(run_every=crontab(minute=0, hour=0, day_of_week='0-4', ))  # 工作日9点
def say_hello():
    print('Good morning!')
    send_mail('早上好',
              '',
              settings.EMAIL_FROM,
              ['2469257690@qq.com', ],
              html_message='<h2>早上好！工作日愉快..</h2>'
              )
    return True
