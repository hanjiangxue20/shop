from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        当发布时间写的是未来某一天的时候，也返回True
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """was_published_recently() returns False for questions whose pub_date
    is older than 1 day.  假如最近一天没有发布问题"""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
    is within the last day.
        :return:
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published)."""
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        """
        If no questions exist, an appropriate message is displayed.
        :return:
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['last_question_list'], [])


# 增加一些测试来检验 pub_date 在过去的 Question 可以显示出来，而 pub_date 在未来的不可以：
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """The detail view of a question with a pub_date in the future
        returns a 404 not found."""
        future_question = create_question(question_text='Future question', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """The detail view of a question with a pub_date in the past
        displays the question's text."""
        past_question= create_question(question_text='Past question',days=-5)
        url = reverse('polls:detail',args=(past_question.id,))   #注意[past_question.id,] 后面的逗号不能掉！！！
        response = self.client.get(url)
        self.assertContains(response,past_question.question_text)

class QuestionResultViewTests(TestCase):
    def test_future_result(self):
        pass

    def test_past_result(self):
        pass