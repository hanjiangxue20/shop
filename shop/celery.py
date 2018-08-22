#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: 2038770992qq.com

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery



# app = Celery('shop')
# app = Celery('shop',
#              broker='redis://127.0.0.1:6379/5',
#              backend='redis://127.0.0.1:6379/5',
#              include=['shop.tasks'])
app = Celery('shop',
             broker='amqp://zkyr:zkyr1006@192.168.1.137:5672/myvhost',
             backend='amqp://zkyr:zkyr1006@191.168.1.137:5672/myvhost',
             include=['shop.tasks'])

# app.config_from_object('django.conf:settings', namespace='CELERY')# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

if __name__ == '__main__':
    app.start()
