# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


class Activity(models.Model):
    title = models.CharField(max_length=128)
    content = UEditorField(imagePath="activity/images/", filePath="activity/files/")
    responsible_user = models.ForeignKey(User)
    address = models.CharField(max_length=128, blank=True, null=True)
    entry_closing_time = models.DateTimeField()
    start_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    is_alternative = models.BooleanField(default=False)
    alternative_title = models.CharField(max_length=128, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=32)
    SEX_CHOICE = (
        ('M', u'男'),
        ('F', u'女'),
    )
    student_id = models.CharField(max_length=16)
    sex = models.CharField(max_length=1, choices=SEX_CHOICE)
    level = models.SmallIntegerField()
    tel = models.CharField(max_length=11)
    alternative_content = models.TextField(blank=True, null=True)

    activity = models.ForeignKey(Activity)

    def __unicode__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    responsible_user = models.ForeignKey(User)
    is_finished = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)

    activity = models.ForeignKey(Activity)

    def __unicode__(self):
        return self.name



