#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: 2038770992qq.com
from __future__ import absolute_import
from shop import celery_app
from celery import shared_task
from time import sleep
from .models import *
from django.db.models import F


# app =Celery('tasks',broker='redis://127.0.0.1:6379/5',backend='redis://127.0.0.1:6379/5')
@celery_app.task()
def add(x, y):
    return x + y


@celery_app.task
def mul(x, y):
    return x * y


@celery_app.task
def sum(x, y):
    return x + y


@celery_app.task
def incr_readtime(article_id):
    return Article.objects.filter(id=article_id).update(score=F('score')+1)