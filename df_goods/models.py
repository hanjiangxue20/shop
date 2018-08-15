from django.db import models
from tinymce.models import HTMLField


# index首页商品分类信息
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='goods')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)  #总位数5   小数2
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20,default='500g')  #重量
    gclick = models.IntegerField() #人气
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField() #库存
    gcontent = HTMLField()
    gtype = models.ForeignKey(TypeInfo,on_delete=models.CASCADE)
    # gadv = models.BooleanField(default=False)  #是否推荐