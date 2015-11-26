# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    name = models.CharField(max_length=32)
    student_id = models.CharField(max_length=16)
    college = models.CharField(max_length=16)
    tel = models.CharField(max_length=11)
    is_public_tel = models.BooleanField(default=False)
    SEX_CHOICE = (
        ('M', u'男'),
        ('F', u'女'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICE)
    level = models.SmallIntegerField()
    birthday = models.DateField()
    qq = models.CharField(max_length=32)
    is_public_qq = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='./user/photo/%Y/%m/%d/')
    is_publisher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=128)
    user = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name
