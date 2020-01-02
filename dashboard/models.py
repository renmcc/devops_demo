from django.db import models

# Create your models here.

class Idc(models.Model):
    name = models.CharField("机房名称",max_length=32)
    address = models.CharField("机房地址",max_length=200)
    phone = models.CharField("机房联系电话",max_length=15)
    email = models.EmailField("机房联系email")
    letter = models.CharField("idc 字母简称",max_length=5)

    class Meta:
        db_table = "dashboard_idc"

class User(models.Model):
    username = models.CharField("用户登录名",max_length=20)
    first_name = models.CharField("first name", max_length=30)

    class Meta:
        db_table = "dashboard_user"

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

