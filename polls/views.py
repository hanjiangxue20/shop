from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic


# #
#     问题索引页——展示最近的几个投票问题。
#     问题详情页——展示某个投票的问题和不带结果的选项列表。
#     问题结果页——展示某个投票的结果。
#     投票处理器——用于响应用户为某个问题的特定选项投票的操作。

def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:10]
    # template = loader.get_template('polls/index.html')
    context = {
        'last_question_list': last_question_list,
    }
    # output = ', '.join([q.question_text for q in last_question_list])
    # response = Question.objects.all()
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
    # 注意到，我们不再需要导入 loader 和 HttpResponse 。
    # 不过如果你还有其他函数（比如说 detail, results, 和 vote ）
    # 需要用到它的话，就需要保持 HttpResponse 的导入。


def detail(request, question_id):
    # try:
    #     question= Question.objects.get(pk= question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    # # return HttpResponse('you are looking at qeustion %s' % question_id)
    # return render(request,'polls/detail.html',{'question':question})

    # 一个快捷函数： get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# 也有 get_list_or_404() 函数，工作原理和 get_object_or_404() 一样，除了 get() 函数被换成了 filter() 函数。
# 如果列表为空的话会抛出 Http404 异常。


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button

        # return HttpResponse("you are voting on question %s." % question_id)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


#     在增加 Choice 的得票数之后，代码返回一个 HttpResponseRedirect 而不是常用的 HttpResponse 、
# HttpResponseRedirect 只接收一个参数：用户将要被重定向的 URL（请继续看下去，
# 我们将会解释如何构造这个例子中的 URL）构造函数中使用 reverse() 函数。这个函数避免了我们在视图函数中硬编码 URL。
# 它需要我们给出我们想要跳转的视图的名字和该视图所对应的 URL 模式中需要给该视图提供的参数。
# reverse() 调用将返回一个这样的字符串：'/polls/3/results/'
# 其中 3 是 question.id 的值。重定向的 URL 将调用 'results' 视图来显示最终的页面

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # response = "you are looking at the results of question % s"
    # return HttpResponse(response % question_id)
    return render(request, 'polls/results.html', {'question': question})


# # 使用通用视图，
class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'last_question_list'

    # last_question_list = Question.objects.order_by('-pub_date')[:10]
    # 对于 ListView， 自动生成的 context 变量是 question_list。为了覆盖这个行为，我们提供 context_object_name 属性，
    # 表示我们想使用 last_question_list传递给了 polls/index.html 模板。作为一种替换方案，你可以改变你的模板来匹配新的 context 变量
    # —— 这是一种更便捷的方法，告诉 Django 使用你想使用的变量名。

    def get_queryset(self):
        """Return the last ten published questions"""
        return Question.objects.order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    # 每个通用视图需要知道它将作用于哪个模型。 这由 model 属性提供
    model = Question
    # template_name 属性是用来告诉 Django 使用一个指定的模板名字，而不是自动生成的默认名字。
    # 默认名字:<app name>/<model name>_detail.html 的模板。在我们的例子中，默认它将使用 "polls/question_detail.html" 模板
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
