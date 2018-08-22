#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: 2038770992qq.com
from __future__ import absolute_import
from shop.celery import app
from celery import shared_task
from time import sleep


# app =Celery('tasks',broker='redis://127.0.0.1:6379/5',backend='redis://127.0.0.1:6379/5')
@app.task()
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@shared_task
def sum(x, y):
    return x + y
