from __future__ import absolute_import
import pymysql
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
# 确保django运行之前,celery启动完成
from .celery import app as celery_app


pymysql.install_as_MySQLdb()
