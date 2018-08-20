from django.contrib import admin

from .models import Question, Choice


class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text']


# 通过 TabularInline``（替代 ``StackedInline ），关联对象以一种表格式的方式展示，显得更加紧凑
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # 有三个关联的选项插槽


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text']
    # fieldsets = [
    #     (None, {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # 过滤器
    search_fields = ['question_text']
    list_per_page = 10  #10

    inlines = [ChoiceInline]  # 告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 3 个足够的选项字段。”


# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)

# 这是一种很低效地添加“选项”的方法。更好的办法是在你创建“投票”对象时直接添加好几个选项。
# admin.site.register(Choice)
# admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Choice, ChoiceAdmin)
