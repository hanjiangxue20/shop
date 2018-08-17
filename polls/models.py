import datetime

from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):  # 添加一个自定义的方法 如果 Question 是在一天之内发布的，bug:时间是未来时候
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        #   修复这个 bug
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)  # 选项描述
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
