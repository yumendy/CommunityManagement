# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=16, null=True, blank=True)),
                ('summery', models.TextField(null=True, blank=True)),
                ('img', models.ImageField(upload_to=b'/carousel/image/%Y/%m/%d/')),
                ('target_url', models.URLField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('show_order', models.IntegerField(default=0)),
                ('on_show', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['show_order', '-create_time'],
                'verbose_name': '\u8f6e\u64ad',
                'verbose_name_plural': '\u8f6e\u64ad',
            },
        ),
    ]
