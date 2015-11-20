# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navitem',
            name='url',
            field=models.CharField(max_length=4096, null=True, verbose_name='\u6307\u5411\u94fe\u63a5', blank=True),
        ),
    ]
