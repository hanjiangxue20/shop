#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: 2038770992qq.com

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

app = Celery('shop')
# redis
# app = Celery('shop',
#              broker='redis://:zkyr1006@127.0.0.1:6379/10',
#              backend='redis://:zkyr1006@127.0.0.1:6379/10',
#              include=['shop.tasks'])
# RabbitMQ
# app = Celery('shop',
#              broker='amqp://zkyr:zkyr1006@111.207.68.150:5672/myvhost',
#              backend='amqp://zkyr:zkyr1006@111.207.68.150:5672/myvhost',
#              include=['shop.tasks'])

# app = Celery('shop',
#              broker='amqp://zkyr:zkyr1006@192.168.1.137:5672/myvhost',
#              backend='redis://:zkyr1006@127.0.0.1:6379/10',
#              )
app.config_from_object('django.conf:settings',namespace='CELERY')  # Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
