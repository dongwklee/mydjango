# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160910_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
