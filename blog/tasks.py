#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: 2038770992qq.com
from __future__ import absolute_import

# from django_redis import cache

from shop import celery_app
from celery import shared_task
from celery.utils.log import get_task_logger
from time import sleep
from .models import *
from django.db.models import F

logger= get_task_logger(__name__)
# app =Celery('tasks',broker='redis://127.0.0.1:6379/5',backend='redis://127.0.0.1:6379/5')
@celery_app.task()
def add(x, y):
    return x + y


@shared_task
def sum(x, y):
    return x + y

@shared_task(ignore_result=True)
def log_result(result):
    logger.info('log_result got: %r',result)

@celery_app.task
def mul(x, y):
    return x * y


@celery_app.task
def incr_readtime(article_id):
    return Article.objects.filter(id=article_id).update(score=F('score') + 1)

@celery_app.task(bind=True)
def mytask(self):
    # cache.set(self.request.id,'Running')
    pass

@celery_app.task
def create_blog(name,tagline):
    Blog.objects.create(name=name,tagline=tagline)