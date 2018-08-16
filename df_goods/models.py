from django.db import models
from tinymce.models import HTMLField  # 使用富文本编辑框要在settings文件中安装


# 将一对多的关系维护在GoodsInfo中维护，另外商品信息与分类信息都属于重要信息需要使用逻辑删除

# index首页商品分类信息
class TypeInfo(models.Model):  # 商品分类信息  水果 海鲜等
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    def __str__(self):  # 这里定义在admin中要显示的内容
        return self.ttitle.encode('utf-8')


class GoodsInfo(models.Model):
    '''#具体商品信息'''
    gtitle = models.CharField(max_length=20)  # 商品的名称
    gpic = models.ImageField(upload_to='goods')  # 关联图片目录
    gprice = models.DecimalField(max_digits=5, decimal_places=2)  # 总位数5   小数2
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    gunit = models.CharField(max_length=20, default='500g')  # 重量 #商品单位kg或者个数
    gclick = models.IntegerField()  # 人气  #商品点击量
    gjianjie = models.CharField(max_length=200)  # 商品简介
    gkucun = models.IntegerField()  # 库存
    gcontent = HTMLField()  # 商品介绍
    gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE)
    # gadv = models.BooleanField(default=False)  #是否推荐

    def __str__(self):
        return self.gtitle.encode('utf-8')
    # python3中 __str__ 不能接收bytes类型的数据，这和python2/3的编解码方式是有关系的。
