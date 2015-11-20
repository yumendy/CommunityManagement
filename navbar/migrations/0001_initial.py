# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default='New page', max_length=8, verbose_name='\u6807\u9898')),
                ('url', models.URLField(null=True, verbose_name='\u6307\u5411\u94fe\u63a5', blank=True)),
                ('show_order', models.SmallIntegerField(default=0, verbose_name='\u5c55\u793a\u987a\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['show_order', '-create_time'],
                'verbose_name': '\u5bfc\u822a\u6761',
                'verbose_name_plural': '\u5bfc\u822a\u6761',
            },
        ),
    ]
