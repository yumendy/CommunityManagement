from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Essay(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User)
    publish_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    show_times = models.IntegerField(default=0)
    content = UEditorField(imagePath="article/images/", filePath="article/files/")

    def __unicode__(self):
        return self.title
