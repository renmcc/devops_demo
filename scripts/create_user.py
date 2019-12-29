#!/usr/bin/env python
#coding:utf-8
#__time__: 2019/12/29 15:42
#__author__ = 'ren_mcc'

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops_demo.settings")
django.setup()
from django.contrib.auth.models import User


username = 'ren'

for i in range(1000):
    name = "{}_{}".format(username, i)
    email = "{}@text.com".format(name)
    User.objects.create_user(name,email, '123')