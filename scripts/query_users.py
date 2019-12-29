#!/usr/bin/env python
#coding:utf-8
#__time__: 2019/12/29 15:53
#__author__ = 'ren_mcc'

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops_demo.settings")
django.setup()
from django.contrib.auth.models import User

userlist = User.objects.all()[:10]
print(userlist)
print(userlist.values())

print(list(userlist.values("username","email")))