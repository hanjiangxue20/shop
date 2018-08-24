from django.db import models


# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):  # __str__ on Python 3
        return self.name

# 假设一篇文章只有一个作者(Author)，一个作者可以有多篇文章(Article)，一篇文章可以有多个标签（Tag)。
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10,default=None,blank=True)
    addr = models.TextField(default=None,blank=True)
    email = models.EmailField()

    def __str__(self):  # __str__ on Python 3
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField()  # 文章的打分
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):  # __str__ on Python 3
        return self.headline


class Add(models.Model):
    task_id= models.CharField(max_length=128)
    first = models.IntegerField() # 第一加数
    second = models.IntegerField()
    result= models.IntegerField()#结果
    log_date=models.DateTimeField() #存储开始时间
