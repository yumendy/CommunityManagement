# coding=utf-8
from django.db import models


class NavItem(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=8, default=u'New page')
    url = models.CharField(verbose_name=u'指向链接', max_length=4096, blank=True, null=True)
    show_order = models.SmallIntegerField(verbose_name=u'展示顺序', default=0)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'导航条'
        ordering = ['show_order', '-create_time']

    def __unicode__(self):
        return self.title
