#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: 2038770992qq.com

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")

import django

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


def main():
    from blog.models import Author
    # Author.objects.all().delete()
    # AuthorList=[]
    # with open('author.txt') as f:
    #     for line in f:
    #         name ,email = line.split('#')
    #         author=Author(name=name,email=email,qq='',addr='')
    #         AuthorList.append(author)
    #         # Author.objects.create(name=name,email=email,qq='',addr='')
    #         # Author.objects.get_or_create(name=name,email=email,qq='',addr='') #比较慢
    #     f.close()
    #     Author.objects.bulk_create(AuthorList)

    # Blog.objects.create()每保存一条就执行一次SQL，而bulk_create()是执行一条SQL存入多条数据，
    # 做会快很多！当然用列表解析代替 for 循环会更快！！
    AuthorList = []
    f = open('author.txt')
    for line in f:
        parts = line.split('#')
        AuthorList.append(Author(name=parts[0], email=parts[1], qq='', addr=''))
        # Author.objects.create(name=name,email=email,qq='',addr='')
        # Author.objects.get_or_create(name=name,email=email,qq='',addr='') #比较慢
    f.close()
    # 以上四行 也可以用 列表解析 写成下面这样
    # BlogList = [Blog(title=line.split('****')[0], content=line.split('****')[1]) for line in f]
    Author.objects.bulk_create(AuthorList)


if __name__ == '__main__':
    main()
    print('Done!')
