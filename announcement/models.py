from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Announcement(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'announcement of ' + str(self.create_time)
