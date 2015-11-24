# coding=utf-8
from django.db import models


class Carousel(models.Model):
    title = models.CharField(max_length=16, blank=True, null=True)
    summery = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='./carousel/image/%Y/%m/%d/')
    target_url = models.URLField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    show_order = models.IntegerField(default=0)
    on_show = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = verbose_name = u'轮播'
        ordering = ['show_order', '-create_time']

    def __unicode__(self):
        return self.title
