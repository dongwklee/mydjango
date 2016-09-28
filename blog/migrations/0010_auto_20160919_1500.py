# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_postimage_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='text',
        ),
        migrations.AddField(
            model_name='postimage',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
