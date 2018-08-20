#!/usr/bin/python3
#-*-coding:utf-8-*-
# Author: 2038770992qq.com

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")

import django
if django.VERSION >=(1,7):#自动判断版本
    django.setup()


def main():
    from blog.models import Author
    # Author.objects.all().delete()
    with open('author.txt') as f:
        for line in f:
            name ,email = line.split('#')
            # Author.objects.create(name=name,email=email,qq='',addr='')
            Author.objects.get_or_create(name=name,email=email,qq='',addr='')
        f.close()


if __name__ == '__main__':
    main()
    print('Done!')


