# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160919_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='author',
        ),
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(to='blog.Post', related_name='image_set'),
        ),
    ]
