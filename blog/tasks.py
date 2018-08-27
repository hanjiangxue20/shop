#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: 2038770992qq.com
from __future__ import absolute_import
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
              ['2469257690@qq.com',],
              html_message=msg
              )
    # sleep(2)
    print('send email success!')
    return True
