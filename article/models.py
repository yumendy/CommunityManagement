from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Essay(models.Model):
    title = models.CharField(max_length=128)
    publish_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    show_times = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class Blog(Essay):
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)
    content = UEditorField(imagePath="article/blog/images/", filePath="article/blog/files/")


class PurePage(Essay):
    content = UEditorField(imagePath="article/pure_page/images/", filePath="article/pure_page/files/")

    def get_absolute_url(self):
        return reverse('pure-page-detail', args=[str(self.id)])
