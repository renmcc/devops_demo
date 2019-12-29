#!/usr/bin/env python
#coding:utf-8
#__time__: 2019/12/29 16:54
#__author__ = 'ren_mcc'

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops_demo.settings")
django.setup()
from django.contrib.auth.models import User
from django.core.paginator import Paginator

queryset = User.objects.all()

paginator = Paginator(queryset, 10)

print(paginator.count)
print(paginator.num_pages)

#获取page对象
page = paginator.page(10)
#查看当前页的元素
print(page.object_list)
